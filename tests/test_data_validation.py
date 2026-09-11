"""Testes de validação de dados e integridade dos schemas."""

from src.api.schemas import TriageInput, TriageOutput
import pytest
from pydantic import ValidationError


def test_triage_input_valid() -> None:
    """Testa se o schema de entrada aceita textos clínicos válidos."""
    payload = TriageInput(abstract="Patient complains of severe chest pain.")
    assert payload.abstract == "Patient complains of severe chest pain."


def test_triage_input_empty() -> None:
    """Testa se o schema rejeita entradas vazias."""
    with pytest.raises(ValidationError):
        TriageInput(abstract="")


def test_triage_output_valid() -> None:
    """Testa se o schema de saída valida rótulos e probabilidades corretas."""
    output = TriageOutput(condition_label=1, probability=0.95)
    assert output.condition_label == 1
    assert output.probability == 0.95
