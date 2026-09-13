from datetime import datetime, timedelta

try:
    from airflow import DAG
    from airflow.operators.bash import BashOperator
except ImportError:
    # Apenas para evitar erro ao ler o arquivo fora do container do Airflow
    DAG = None
    BashOperator = None

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

if DAG:
    with DAG(
        "medical_triage_training_pipeline",
        default_args=default_args,
        description="DAG simples para simular o pipeline de treino e preprocessamento",
        schedule_interval="@weekly",
        start_date=datetime(2026, 1, 1),
        catchup=False,
    ) as dag:
        preprocess_task = BashOperator(
            task_id="run_preprocessing",
            bash_command="cd /opt/airflow && uv run python src/stages/preprocess.py",
        )

        train_task = BashOperator(
            task_id="run_training",
            bash_command="cd /opt/airflow && uv run python src/stages/train.py",
        )

        preprocess_task >> train_task
