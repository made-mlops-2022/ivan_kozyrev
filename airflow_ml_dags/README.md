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

```
