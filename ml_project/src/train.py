import hydra
from hydra.core.config_store import ConfigStore

from ml_project.src.custom_logger import get_logger
from ml_project.src.customdataclasses import MainParam
from ml_project.src.data import read_data, split_feature_target, split_train_test_data
from ml_project.src.model import train_model, save_model

cs = ConfigStore.instance()
cs.store(name='main_param', node=MainParam)
logger = get_logger()


@hydra.main(version_base=None, config_path='../config', config_name='main_config')
def run_train(conf: MainParam):
    logger.info('model = %s', conf.model.model_name)
    data = read_data(conf.model.path_2_raw_data_input)
    logger.info('read data')

    x, y = split_feature_target(data, conf.param_4_input_data.target_column)
    logger.info('split features target')

    x_train, x_test, y_train, y_test = split_train_test_data(x, y, conf.model)
    logger.info('split train tests')

    x_test.to_csv('data/test/test.csv', index=False)
    logger.info('start train model')
    model = train_model(x_train, y_train, conf.model)
    logger.info('end train model')

    save_model(model, conf.model.path_2_ready_model)
    logger.info('model saved')


if __name__ == '__main__':
    run_train()
