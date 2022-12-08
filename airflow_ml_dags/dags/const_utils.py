import os
from datetime import timedelta
from airflow.models import Variable
from airflow.utils.email import send_email_smtp

LOCAL_DATA_DIR = Variable.get('local_data_dir')


def callable_wait_file_exist(path2file: str):
    return os.path.exists(path2file)


def callback_fail_email(context):
    dag_run = context.get('dag_run')
    send_email_smtp(to=default_args['email'], subject=dag_run)


default_args = {
    "owner": "ivan kozyrev",
    "email": ["ivankozyrev02@mail.ru"],
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    'on_failure_callback': callback_fail_email
}
