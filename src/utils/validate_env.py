"""Módulo para validação de ambiente e estrutura de diretórios."""

from pathlib import Path


def validate_environment() -> None:
    """Verifica e cria os diretórios essenciais para o funcionamento do pipeline."""
    root_dir = Path(__file__).resolve().parents[2]

    required_dirs = [
        root_dir / "data" / "processed",
        root_dir / "models",
        root_dir / "src" / "models",
        root_dir / "src" / "stages",
        root_dir / "src" / "utils",
    ]

    for directory in required_dirs:
        directory.mkdir(parents=True, exist_ok=True)

    print("Ambiente validado com sucesso. Diretórios verificados/criados.")


if __name__ == "__main__":
    validate_environment()
