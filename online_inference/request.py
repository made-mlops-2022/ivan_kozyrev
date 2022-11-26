import json
import logging

import pandas as pd
import requests

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)

data = pd.read_csv('data4request.csv')
data = data.drop('condition', axis=1)
data4request = data.to_dict(orient='records')

for req in data.to_dict(orient='records'):
    response = requests.post(
        url='http://127.0.0.1:8800/predict',
        data=json.dumps(req)
    )
    logger.info('-----')
    logger.info(f'Code -> {response.status_code}')
    logger.info(f'Msg -> {response.json()}')
