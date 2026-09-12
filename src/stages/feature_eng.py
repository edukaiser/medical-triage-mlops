"""Script responsável pela engenharia de recursos e vetorização TF-IDF."""

from pathlib import Path
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


def main() -> None:
    """Executa a vetorização TF-IDF nos dados limpos de treino e teste."""
    base_dir = Path(__file__).resolve().parents[2]
    processed_dir = base_dir / "data" / "processed"
    models_dir = base_dir / "models"
    models_dir.mkdir(parents=True, exist_ok=True)

    # Carregar dados limpos
    train_df = pd.read_csv(processed_dir / "medical_tc_train_clean.csv")
    test_df = pd.read_csv(processed_dir / "medical_tc_test_clean.csv")

    # Configurar e ajustar o TfidfVectorizer
    tfidf = TfidfVectorizer(max_features=5000, stop_words="english")

    train_texts = train_df["clean_abstract"].fillna("").values
    test_texts = test_df["clean_abstract"].fillna("").values

    # Ajustar no treino e transformar ambos
    tfidf.fit_transform(train_texts)
    tfidf.transform(test_texts)

    # Salvar o vetorizador treinado para uso posterior
    vectorizer_path = models_dir / "tfidf_vectorizer.pkl"
    joblib.dump(tfidf, vectorizer_path)
    print(f"Vetorizador TF-IDF salvo com sucesso em: {vectorizer_path}")


if __name__ == "__main__":
    main()
