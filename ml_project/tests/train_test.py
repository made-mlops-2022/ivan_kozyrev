import unittest
from unittest import TestCase, mock
from logging import Logger

from ml_project.src.data import split_feature_target, split_train_test_data
from ml_project.src.customdataclasses import ModelParam
from ml_project.src.model import train_model

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import recall_score
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier

import pandas as pd
import os


class TrainTest(TestCase):

    def test_split_feature_target(self):
        test_df = pd.DataFrame(data={"1": [1, 1, 1], "2": [2, 2, 2], "condition": [0, 0, 0]})

        test_features, test_target = split_feature_target(test_df, "condition")
        self.assertEqual(test_features.shape, (3, 2))
        self.assertListEqual(list(test_target), [0, 0, 0])

        test_features, test_target = split_feature_target(test_df, "2")
        self.assertEqual(test_features.shape, (3, 2))
        self.assertEqual(list(test_target), [2, 2, 2])

    def test_change_model(self):
        test_df = pd.DataFrame(data={"1": [1, 1, 1], "2": [2, 2, 2], "condition": [0, 1, 0]})

        test_features, test_target = split_feature_target(test_df, "condition")

        test_param = ModelParam
        test_param.grid = False
        test_param.random_state = 1
        test_param.max_iter = 1
        test_param.max_depth = 1

        test_param.model_name = 'DecisionTreeClassifier'
        model = train_model(test_features, test_target, test_param)
        self.assertIsInstance(model, DecisionTreeClassifier)

        test_param.model_name = 'LogisticRegression'
        model = train_model(test_features, test_target, test_param)
        self.assertIsInstance(model, LogisticRegression)

        test_param.model_name = 'CatBoost'
        with self.assertRaises(NotImplementedError):
            train_model(test_features, test_target, test_param)

        #
    # def test_create_pipeline(self):
    #
    #     logger.info("Start test pipeline creation")
    #     model = LogisticRegression()
    #     pipeline = create_inference_pipeline(model)
    #     self.assertIsInstance(pipeline, Pipeline)
    #     self.assertEqual(pipeline.steps, [("model_part", model)])
    #     logger.info("Finish test pipeline creation")
