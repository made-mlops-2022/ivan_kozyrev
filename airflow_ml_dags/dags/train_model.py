from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sensors.python import PythonSensor
from airflow.utils.dates import days_ago
from docker.types import Mount

from const_utils import LOCAL_DATA_DIR, default_args, callable_wait_file_exist

with DAG(
        'train',
        default_args=default_args,
        schedule_interval='@weekly',
        start_date=days_ago(7)
) as dag:
    wait_data = PythonSensor(
        task_id='wait-for-data',
        python_callable=callable_wait_file_exist,
        op_args=['/opt/airflow/data/raw/{{ ds }}/data.csv'],
        timeout=6000,
        poke_interval=10,
        retries=100,
        mode="poke"
    )

    wait_target = PythonSensor(
        task_id='wait-for-target',
        python_callable=callable_wait_file_exist,
        op_args=['/opt/airflow/data/raw/{{ ds }}/target.csv'],
        timeout=6000,
        poke_interval=10,
        retries=100,
        mode="poke"
    )

    preprocess = DockerOperator(
        image='airflow-preprocess',
        command='--input-dir /data/raw/{{ ds }}',
        task_id='docker-airflow-preprocess',
        network_mode='bridge',
        do_xcom_push=False,
        auto_remove=True,
        mounts=[Mount(source=LOCAL_DATA_DIR, target='/data', type='bind')]
    )

    split = DockerOperator(
        image='airflow-split',
        command='--input-dir /data/raw/{{ ds }} --output-dir /data/splitted/{{ ds }}',
        network_mode='bridge',
        task_id='docker-airflow-split',
        do_xcom_push=False,
        auto_remove=True,
        mounts=[Mount(source=LOCAL_DATA_DIR, target='/data', type='bind')]
    )

    train = DockerOperator(
        image='airflow-train',
        command='--input-dir /data/splitted/{{ ds }} --output-dir /data/models/{{ ds }}',
        network_mode='bridge',
        task_id='docker-airflow-train',
        do_xcom_push=True,
        auto_remove=True,
        mounts=[Mount(source=LOCAL_DATA_DIR, target='/data', type='bind')],
    )

    validate = DockerOperator(
        image='airflow-validate',
        command='--input-dir /data/splitted/{{ ds }} --model-dir /data/models/{{ ds }} --output-dir /data/metrics/{{ ds }}',
        network_mode='bridge',
        task_id='docker-airflow-validate',
        do_xcom_push=False,
        auto_remove=True,
        mounts=[Mount(source=LOCAL_DATA_DIR, target='/data', type='bind')]
    )

    [wait_data, wait_target] >> preprocess >> split >> train >> validate
