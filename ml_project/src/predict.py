import click as click
import pandas as pd

from custom_logger import get_logger
from data import read_data
from model import predict_model, load_model

logger = get_logger()


@click.command()
@click.argument('path2model', type=click.Path(exists=True), default='model/logreg/finalized_model.sav')
@click.argument('path2data', type=click.Path(exists=True), default='data/tests/tests.csv')
@click.argument('path2predict', default='data/predict/predict.csv')
def run_predict(path2model: str, path2data: str, path2predict: str):
    x_test = read_data(path2data)
    logger.info('read data for predict')

    loaded_model = load_model(path2model)
    logger.info('chosen model loaded')

    result = predict_model(loaded_model, x_test)
    logger.info('got predict')
    pd.DataFrame(result).to_csv(path2predict, index=False)
    logger.info('wrote predict to file')


if __name__ == "__main__":
    run_predict()
