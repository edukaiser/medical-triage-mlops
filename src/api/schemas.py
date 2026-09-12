"""Schemas Pydantic para validação de entrada e saída da API."""

from pydantic import BaseModel, field_validator


class TriageInput(BaseModel):
    """Schema para o texto clínico de entrada."""

    abstract: str

    @field_validator("abstract")
    @classmethod
    def validate_abstract_not_empty(cls: type["TriageInput"], value: str) -> str:
        """Garante que o texto clínico não está vazio ou em branco."""
        if not value or not value.strip():
            raise ValueError("O campo 'abstract' não pode estar vazio.")
        return value


class TriageOutput(BaseModel):
    """Schema para a resposta da predição."""

    condition_label: int
    probability: float
