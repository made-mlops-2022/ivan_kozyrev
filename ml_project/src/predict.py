import hydra
import pandas as pd
from hydra.core.config_store import ConfigStore

from custom_logger import get_logger
from data import read_data
from ml_project.src.customdataclasses import PredictParam
from model import predict_model, load_model

cs = ConfigStore.instance()
cs.store(name='predict_param', node=PredictParam)
logger = get_logger()


@hydra.main(version_base=None, config_path='../config', config_name='predict_config')
def run_predict(conf: PredictParam):
    x_test = read_data(conf.path_2_data)
    logger.info('read data for predict')

    loaded_model = load_model(conf.path_2_model)
    logger.info('chosen model loaded')

    result = predict_model(loaded_model, x_test)
    logger.info('got predict')
    pd.DataFrame(result).to_csv(conf.path_2_predict, index=False)
    logger.info('wrote predict to file')


if __name__ == "__main__":
    run_predict()
