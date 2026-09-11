"""Testes para funções utilitárias do projeto."""

from pathlib import Path


def test_project_root_structure() -> None:
    """Valida se a estrutura de diretórios base do projeto está acessível."""
    root_dir = Path(__file__).resolve().parents[1]
    assert (root_dir / "src").exists()
    assert (root_dir / "tests").exists()
