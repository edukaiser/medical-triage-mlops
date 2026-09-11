"""Testes automatizados para os módulos de pré-processamento de dados."""

from pathlib import Path
import joblib
import pytest


def test_vectorizer_artifact_exists() -> None:
    """Verifica se o vetorizador TF-IDF existe e pode ser carregado."""
    root_dir = Path(__file__).resolve().parents[1]
    vectorizer_path = root_dir / "models" / "tfidf_vectorizer.pkl"

    assert vectorizer_path.exists(), "Artefato tfidf_vectorizer.pkl não encontrado."
    vectorizer = joblib.load(vectorizer_path)
    assert vectorizer is not None


def test_vectorizer_transformation() -> None:
    """Testa se o vetorizador TF-IDF transforma textos corretamente.

    Em matrizes esparsas.
    """
    root_dir = Path(__file__).resolve().parents[1]
    vectorizer_path = root_dir / "models" / "tfidf_vectorizer.pkl"

    if not vectorizer_path.exists():
        pytest.skip("Vetorizador não encontrado, pulando teste de transformação.")

    vectorizer = joblib.load(vectorizer_path)
    sample_text = ["Patient reports severe headache and fever."]
    features = vectorizer.transform(sample_text)

    assert features.shape[0] == 1
    assert features.shape[1] > 0
