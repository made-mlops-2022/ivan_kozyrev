from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from docker.types import Mount

from const_utils import LOCAL_DATA_DIR, default_args

with DAG(
        'get_data',
        default_args=default_args,
        schedule_interval='@daily',
        start_date=days_ago(7),
) as dag:
    generate = DockerOperator(
        image='airflow-get-data',
        command='--output-dir /data/raw/{{ ds }}',
        network_mode='bridge',
        task_id='docker-airflow-get-data',
        do_xcom_push=False,
        auto_remove=True,
        mounts=[Mount(source=LOCAL_DATA_DIR, target='/data', type='bind')]
    )

    split_target = DockerOperator(
        image='airflow-split-target',
        command='--input-dir /data/raw/{{ ds }} --target-colm condition',
        task_id='docker-airflow-split-target',
        network_mode='bridge',
        do_xcom_push=False,
        auto_remove=True,
        mounts=[Mount(source=LOCAL_DATA_DIR, target='/data', type='bind')]
    )

    generate >> split_target
