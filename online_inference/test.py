import json

import pytest
from fastapi.testclient import TestClient

from main import app, start

client = TestClient(app)


@pytest.fixture(scope='session', autouse=True)
def start_test():
    start()


def test_model_disease():
    request = {
        "age": 62,
        "sex": 1,
        "cp": 1,
        "trestbps": 120,
        "chol": 281,
        "fbs": 0,
        "restecg": 2,
        "thalach": 103,
        "exang": 0,
        "oldpeak": 1.4,
        "slope": 1,
        "ca": 1,
        "thal": 2
    }
    response = client.post(
        url='/predict',
        content=json.dumps(request)
    )
    assert response.status_code == 200
    assert response.json() == {'condition': 'disease', "predict": '1'}


def test_model_no_disease():
    request = {
        "age": 52,
        "sex": 1,
        "cp": 0,
        "trestbps": 152,
        "chol": 298,
        "fbs": 1,
        "restecg": 0,
        "thalach": 178,
        "exang": 0,
        "oldpeak": 1.2,
        "slope": 1,
        "ca": 0,
        "thal": 2
    }

    response = client.post(
        url='/predict',
        content=json.dumps(request)
    )
    assert response.status_code == 200
    assert response.json() == {'condition': 'no disease', "predict": '0'}


def test_health_model():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'code': 200, 'msg': 'all is ready'}


def test_miss_field_data():
    request = {
        "sex": 1,
        "cp": 0,
        "trestbps": 152,
        "chol": 298,
        "fbs": 1,
        "restecg": 0,
        "thalach": 178,
        "exang": 0,
        "oldpeak": 1.2,
        "slope": 1,
        "ca": 0,
        "thal": 2
    }
    response = client.post(
        url='/predict',
        content=json.dumps(request)
    )
    assert response.status_code == 422
    assert response.json()['detail'][0]['msg'] == 'field required'


def test_bad_literal_value_data():
    request = {
        'age': 53,
        'sex': 0,
        'cp': 3,
        'trestbps': 155,
        'chol': 165,
        'fbs': 1,
        'restecg': 0,
        'thalach': 91,
        'exang': 0,
        'oldpeak': 1.7,
        'slope': 0,
        'ca': 0,
        'thal': 100
    }
    response = client.post(
        url='/predict',
        content=json.dumps(request)
    )
    assert response.status_code == 422
    assert response.json()['detail'][0]['msg'] == 'unexpected value; permitted: 0, 1, 2'


def test_bad_float_value_data():
    request = {
        'age': 23,
        'sex': 1,
        'cp': 3,
        'trestbps': 155,
        'chol': 165,
        'fbs': 1,
        'restecg': 0,
        'thalach': 91,
        'exang': 0,
        'oldpeak': 1000,
        'slope': 0,
        'ca': 0,
        'thal': 2
    }
    response = client.post(
        url='/predict',
        content=json.dumps(request)
    )
    assert response.status_code == 400
    assert response.json()['detail'] == 'oldpeak must be in range [0-9]'
