"""Testes de sanidade geral do ambiente e do ecossistema da aplicação."""

import fastapi
import pydantic
import sklearn


def test_environment_dependencies() -> None:
    """Garante que as principais dependências de ML e API estão carregadas."""
    assert fastapi.__version__ is not None
    assert pydantic.__version__ is not None
    assert sklearn.__version__ is not None
