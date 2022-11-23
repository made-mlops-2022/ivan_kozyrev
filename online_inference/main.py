import os

import pandas as pd
from fastapi import FastAPI
from joblib import load

from data_model_valid import Patient

app = FastAPI()

model = None


@app.on_event("startup")
def start():
    path2model = os.getenv('PATH2MODEL')
    # path2model = 'finalized_model.sav'
    global model
    model = load(path2model)


@app.post('/predict')
async def make_smth(cur_patient: Patient):
    x_data = pd.DataFrame.from_records([cur_patient.dict()])
    predict = model.predict(x_data)
    condition = 'no disease' if not predict[0] else 'disease'
    return {'condition': condition, "predict": str(predict[0])}


@app.get('/health')
async def check_health():
    if model:
        return {'code': 200, 'msg': 'all is ready'}

    return {'code': 592, 'msg': 'server not ready'}
