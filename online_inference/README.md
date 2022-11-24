# HW_2
### build docker image
- from online_inference:
```
docker build -t online_reference .
```

- from public DockerHub:
```
docker pull oneokoz/online_reference
```

### run docker container
```
docker run -d -p 8800:8800 online_reference
```

Service is running on http://127.0.0.1:8800


### run tests
```
docker exec -it <CONTAINER_NAME> bash
python3 -m pytest test_main.py
```

![Alt-текст](https://github.com/made-mlops-2022/ivan_kozyrev/blob/homework2/online_inference/Снимок%20экрана%202022-11-24%20в%2003.11.50.png)
