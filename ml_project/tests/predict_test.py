import os
from unittest import TestCase

from ml_project.src.model import load_model, predict_model
from ml_project.src.data import read_data
import pandas as pd

MODEL_PATH_DIR = "./ml_project/model/"
MODEL_NAME = "/finalized_model.sav"


class PredictTest(TestCase):

    def test_model_load(self):
        model = load_model(MODEL_PATH_DIR + 'logreg' + MODEL_NAME)
        self.assertTrue(model)

        model = load_model(MODEL_PATH_DIR + 'destree' + MODEL_NAME)
        self.assertTrue(model)

        with self.assertRaises(FileNotFoundError):
            load_model('not/exist')

    def test_predict_calc_save(self):
        path_test_data = './ml_project/data/test/test.csv'
        x_test = read_data(path_test_data)
        self.assertTrue(len(x_test))

        model = load_model(MODEL_PATH_DIR + 'logreg' + MODEL_NAME)
        self.assertTrue(model)

        result = predict_model(model, x_test)
        self.assertTrue(model)

        path_predict_data = './ml_project/data/predict/predict.csv'
        pd.DataFrame(result).to_csv(path_predict_data, index=False)
        self.assertTrue(os.path.exists(path_predict_data))
