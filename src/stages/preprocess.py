"""Script responsável pelo pré-processamento e limpeza dos dados brutos."""

import re
from pathlib import Path
import pandas as pd


def clean_text(text: str) -> str:
    """Realiza a limpeza básica de texto em resumos médicos."""
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r"\W+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def main() -> None:
    """Executa o pipeline de pré-processamento para os dados de treino e teste."""
    # Definir caminhos utilizando Pathlib
    base_dir = Path(__file__).resolve().parents[2]
    raw_dir = base_dir / "data" / "raw"
    processed_dir = base_dir / "data" / "processed"
    
    print(f"Procurando dados em: {raw_dir.resolve()}")
    print(f"O arquivo de treino existe? {(raw_dir / 'medical_tc_train.csv').exists()}")
    
    processed_dir.mkdir(parents=True, exist_ok=True)

    # Carregar e processar treino
    train_path = raw_dir / "medical_tc_train.csv"
    if train_path.exists():
        train_df = pd.read_csv(train_path)
        train_df["clean_abstract"] = train_df["medical_abstract"].apply(clean_text)
        train_output = processed_dir / "medical_tc_train_clean.csv"
        train_df.to_csv(train_output, index=False)
        print(f"Treino limpo e salvo em: {train_output}")

    # Carregar e processar teste
    test_path = raw_dir / "medical_tc_test.csv"
    if test_path.exists():
        test_df = pd.read_csv(test_path)
        test_df["clean_abstract"] = test_df["medical_abstract"].apply(clean_text)
        test_output = processed_dir / "medical_tc_test_clean.csv"
        test_df.to_csv(test_output, index=False)
        print(f"Teste limpo e salvo em: {test_output}")


if __name__ == "__main__":
    main()