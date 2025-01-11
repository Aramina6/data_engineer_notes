from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 21),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'ftp_file_processing',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
)

def download_files(**kwargs):
    # Call the file download component
    from file_download.ftp_downloader import download_files_from_ftp
    download_files_from_ftp()

def validate_files(**kwargs):
    # Call the file validation component
    from file_validation.file_validator import validate_files
    validate_files()

def process_files(**kwargs):
    # Call the file processing component
    from file_processing.file_processor import process_files
    process_files()

download_files_task = PythonOperator(
    task_id='download_files',
    python_callable=download_files,
    dag=dag,
)

validate_files_task = PythonOperator(
    task_id='validate_files',
    python_callable=validate_files,
    dag=dag,
)

process_files_task = PythonOperator(
    task_id='process_files',
    python_callable=process_files,
    dag=dag,
)

end_task = BashOperator(
    task_id='end_task',
    bash_command='echo "File processing complete"',
    dag=dag,
)

download_files_task >> validate_files_task >> process_files_task >> end_task
