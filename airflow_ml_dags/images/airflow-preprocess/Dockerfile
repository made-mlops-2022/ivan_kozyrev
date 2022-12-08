FROM python:3.8

COPY ./ /
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt


ENTRYPOINT ["python3", "preprocess.py"]