import logging
from pathlib import Path

import joblib
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer

# Configuração de logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main() -> None:
    """Executa o pipeline de treinamento do modelo.

    Gerando métricas no MLflow e salvando o artefato final.
    """
    root_dir = Path(__file__).resolve().parents[2]
    processed_data_path = root_dir / "data" / "processed" / "medical_tc_train_clean.csv"
    vectorizer_path = root_dir / "models" / "tfidf_vectorizer.pkl"
    model_output_dir = root_dir / "models"
    model_output_path = model_output_dir / "model.pkl"

    model_output_dir.mkdir(parents=True, exist_ok=True)

    logger.info("Carregando dados processados...")
    df_train = pd.read_csv(processed_data_path)

    x_text = df_train["clean_abstract"].fillna("")
    y_train = df_train["condition_label"]

    logger.info("Instanciando e ajustando o TfidfVectorizer...")
    vectorizer = TfidfVectorizer(max_features=5000)
    x_train_features = vectorizer.fit_transform(x_text)

    # Salva o vetorizador treinado para uso posterior na API/inferência
    joblib.dump(vectorizer, vectorizer_path)
    logger.info(f"Vetorizador salvo com sucesso em: {vectorizer_path}")

    # 2. Inicialização do MLflow Tracking
    mlflow.set_experiment("medical-triage-classification")

    with mlflow.start_run(run_name="train_model"):
        logger.info("Iniciando o treinamento do modelo...")

        c_param = 1.0
        max_iter_param = 1000

        mlflow.log_param("model_type", "LogisticRegression")
        mlflow.log_param("C", c_param)
        mlflow.log_param("max_iter", max_iter_param)

        model = LogisticRegression(C=c_param, max_iter=max_iter_param, random_state=42)
        model.fit(x_train_features, y_train)

        predictions = model.predict(x_train_features)
        acc = accuracy_score(y_train, predictions)

        logger.info(f"Acurácia no treino: {acc:.4f}")
        mlflow.log_metric("train_accuracy", acc)

        joblib.dump(model, model_output_path)
        logger.info(f"Modelo salvo com sucesso em: {model_output_path}")

        mlflow.sklearn.log_model(model, "model")
        mlflow.log_artifact(str(model_output_path))
        mlflow.log_artifact(str(vectorizer_path))


if __name__ == "__main__":
    main()
