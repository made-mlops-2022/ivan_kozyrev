# ivan_kozyrev

Для запуска airflow
--------
```
export LOCAL_DATA_DIR=$(pwd)/data
export FERNET_KEY=$(python3 -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")
docker-compose up --build
```
стандартный логин и пароль - admin admin соответственно

для почты надо поменять адерс отправителя и черезе export передать пароль
```
export PASSWORD=YOUR_PASS
```

Для запуска tests
--------
```
docker exec -it airflow_ml_dags_scheduler_1 bash
```
```
pip3 install pytest
python3 -m pytest --disable-warnings tests/test_dags.py
python3 -m pytest --disable-warnings tests/test_dags_compositions.py
```
Результат выполнения

<img width="773" alt="Снимок экрана 2022-12-05 в 02 23 20" src="https://user-images.githubusercontent.com/70657478/205522021-3d0823c3-57da-4413-883b-07189ac73286.png">
