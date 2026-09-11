"""Módulo principal da API FastAPI para predição de triagem médica."""

from contextlib import asynccontextmanager
from pathlib import Path

import joblib
from fastapi import FastAPI, HTTPException
from src.api.schemas import TriageInput, TriageOutput
from collections.abc import AsyncIterator

ml_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Gerencia o ciclo de vida da aplicação carregando.

    Os artefatos de ML na inicialização.
    """
    root_dir = Path(__file__).resolve().parents[2]
    model_path = root_dir / "models" / "model.pkl"
    vectorizer_path = root_dir / "models" / "tfidf_vectorizer.pkl"

    if not model_path.exists() or not vectorizer_path.exists():
        raise RuntimeError(
            "Artefatos do modelo não encontrados. Execute o DVC repro antes.",
        )

    ml_models["model"] = joblib.load(model_path)
    ml_models["vectorizer"] = joblib.load(vectorizer_path)
    yield
    ml_models.clear()


app = FastAPI(
    title="Medical Triage API",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.get("/health", status_code=200)
def health_check() -> dict[str, str]:
    """Retorna o status de funcionamento da API e dos artefatos de ML."""
    model_loaded = "model" in ml_models and "vectorizer" in ml_models
    return {
        "status": "healthy" if model_loaded else "degraded",
        "model_loaded": str(model_loaded),
    }


@app.post("/predict", response_model=TriageOutput)
def predict(payload: TriageInput) -> TriageOutput:
    """Realiza a predição de triagem médica com base no.

    Resumo clínico fornecido.
    """
    model = ml_models.get("model")
    vectorizer = ml_models.get("vectorizer")

    if not model or not vectorizer:
        raise HTTPException(
            status_code=500,
            detail="Modelo não carregado na memória.",
        )

    x_features = vectorizer.transform([payload.abstract])
    prediction = model.predict(x_features)[0]
    probabilities = model.predict_proba(x_features)[0]
    confidence = float(max(probabilities))

    return TriageOutput(
        condition_label=int(prediction),
        probability=confidence,
    )
