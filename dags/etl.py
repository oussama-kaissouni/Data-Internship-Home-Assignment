from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.extract import extract_jobs
from src.transform import clean_and_transform
from src.load import load_to_sqlite

default_args = {
    'start_date': datetime(2023, 1, 1),
}

with DAG('etl_pipeline', default_args=default_args, schedule='@daily') as dag:
    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract_jobs,
        op_kwargs={
            'csv_path': 'source/jobs.csv',
            'output_dir': 'staging/extracted',
        },
    )

    transform_task = PythonOperator(
        task_id='transform',
        python_callable=clean_and_transform,
        op_kwargs={
            'input_dir': 'staging/extracted',
            'output_dir': 'staging/transformed',
        },
    )

    load_task = PythonOperator(
        task_id='load',
        python_callable=load_to_sqlite,
        op_kwargs={
            'input_dir': 'staging/transformed',
            'db_path': 'staging/jobs.db',
        },
    )

    extract_task >> transform_task >> load_task
