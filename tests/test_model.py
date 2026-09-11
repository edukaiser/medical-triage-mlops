"""Testes automatizados para o modelo de machine learning de triagem."""

from pathlib import Path
import joblib
import pytest


def test_model_artifact_exists() -> None:
    """Verifica se o artefato do modelo treinado existe e pode ser carregado."""
    root_dir = Path(__file__).resolve().parents[1]
    model_path = root_dir / "models" / "model.pkl"

    assert model_path.exists(), "Artefato model.pkl não encontrado."
    model = joblib.load(model_path)
    assert model is not None


def test_model_prediction_output() -> None:
    """Testa se o modelo produz previsões e probabilidades coerentes.

    Com base em features vetorizadas.
    """
    root_dir = Path(__file__).resolve().parents[1]
    model_path = root_dir / "models" / "model.pkl"
    vectorizer_path = root_dir / "models" / "tfidf_vectorizer.pkl"

    if not model_path.exists() or not vectorizer_path.exists():
        pytest.skip("Artefatos de modelo ou vetorizador ausentes.")

    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)

    sample_text = ["Acute chest pain and shortness of breath."]
    features = vectorizer.transform(sample_text)

    prediction = model.predict(features)
    probabilities = model.predict_proba(features)

    assert len(prediction) == 1
    assert probabilities.shape[0] == 1
    assert probabilities.shape[1] >= 2
