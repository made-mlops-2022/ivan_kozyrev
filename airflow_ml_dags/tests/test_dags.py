import pytest

from airflow.models import DagBag


@pytest.fixture()
def dagbag():
    return DagBag()


def test_get_data_dag(dagbag):
    dag = dagbag.get_dag(dag_id='get_data')
    assert dagbag.import_errors == {}
    assert dag is not None
    assert len(dag.tasks) == 2


def test_train_model_dag(dagbag):
    dag = dagbag.get_dag(dag_id='train')
    assert dagbag.import_errors == {}
    assert dag is not None
    assert len(dag.tasks) == 6


def test_predict_model_dag(dagbag):
    dag = dagbag.get_dag(dag_id='predict')
    assert dagbag.import_errors == {}
    assert dag is not None
    assert len(dag.tasks) == 3
    print(dag.task_dict)
