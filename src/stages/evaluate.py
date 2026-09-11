import logging
from pathlib import Path

import joblib
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report

# Configuração de logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def main() -> None:
    """Executa a avaliação do modelo treinado no conjunto de teste.

    Gera métricas finais no MLflow e valida o desempenho.
    """
    # 1. Definição de caminhos de forma agnóstica (raiz do projeto)
    root_dir = Path(__file__).resolve().parents[2]
    test_data_path = root_dir / "data" / "processed" / "medical_tc_test_clean.csv"
    vectorizer_path = root_dir / "models" / "tfidf_vectorizer.pkl"
    model_path = root_dir / "models" / "model.pkl"
    metrics_output_dir = root_dir / "metrics"
    metrics_output_path = metrics_output_dir / "scores.json"

    metrics_output_dir.mkdir(parents=True, exist_ok=True)

    logger.info("Carregando dados de teste, vetorizador e modelo...")
    df_test = pd.read_csv(test_data_path)

    x_text = df_test["clean_abstract"].fillna("")
    y_test = df_test["condition_label"]

    vectorizer = joblib.load(vectorizer_path)
    model = joblib.load(model_path)

    logger.info("Transformando textos de teste com o vetorizador...")
    x_test_features = vectorizer.transform(x_text)

    # 2. Inicialização do MLflow Tracking para Avaliação
    mlflow.set_experiment("medical-triage-classification")

    with mlflow.start_run(run_name="evaluate_model"):
        logger.info("Realizando predições no conjunto de teste...")
        predictions = model.predict(x_test_features)

        acc = accuracy_score(y_test, predictions)
        report = classification_report(y_test, predictions, output_dict=True)

        logger.info(f"Acurácia no teste: {acc:.4f}")
        mlflow.log_metric("test_accuracy", acc)

        # Salvando as métricas localmente para o DVC monitorar
        import json

        metrics_data = {"test_accuracy": acc, "classification_report": report}
        with open(metrics_output_path, "w", encoding="utf-8") as f:
            json.dump(metrics_data, f, indent=4)

        logger.info(f"Métricas salvas com sucesso em: {metrics_output_path}")
        mlflow.log_artifact(str(metrics_output_path))


if __name__ == "__main__":
    main()
