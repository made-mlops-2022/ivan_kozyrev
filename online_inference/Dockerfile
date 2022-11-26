FROM python:3.9.7

COPY requirements.txt ./online_inference/
WORKDIR /online_inference
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

ENV PATH2MODEL="finalized_model.sav"
EXPOSE 8800

CMD ["bash","start.sh"]