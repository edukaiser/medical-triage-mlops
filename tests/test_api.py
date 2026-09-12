"""Testes automatizados para os endpoints da API de triagem médica."""

from fastapi.testclient import TestClient
from src.api.main import app


def test_health_check() -> None:
    """Testa se o endpoint /health retorna status 200 e o dicionário de status."""
    with TestClient(app) as client:
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert "status" in data
        assert "model_loaded" in data


def test_predict_endpoint() -> None:
    """Testa se o endpoint /predict retorna status 200.

    E a estrutura esperada de saída.
    """
    with TestClient(app) as client:
        response = client.post(
            "/predict",
            json={
                "abstract": (
                    "Patient presents with acute chest pain and " "shortness of breath."
                ),
            },
        )
        assert response.status_code == 200
        data = response.json()
        assert "condition_label" in data
        assert "probability" in data
        assert isinstance(data["condition_label"], int)
        assert isinstance(data["probability"], float)
