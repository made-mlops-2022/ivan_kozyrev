import pickle
from typing import Dict, Union

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import recall_score
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier

from ml_project.src.customdataclasses import ModelParam

SklearnClassificationModel = Union[DecisionTreeClassifier, LogisticRegression]


def train_model(x_train: np.ndarray, y_train: np.ndarray, model_param: ModelParam):
    if model_param.model_name == 'DecisionTreeClassifier':
        model = DecisionTreeClassifier(random_state=model_param.random_state)
        grid = {'criterion': ['gini', 'entropy'],
                'max_depth': model_param.max_depth}

    elif model_param.model_name == 'LogisticRegression':
        model = LogisticRegression(random_state=model_param.random_state, max_iter=model_param.max_iter)
        grid = {"C": np.logspace(-3, 3, 3),
                "penalty": ["l2"]}
    else:
        raise NotImplementedError()

    if model_param.grid:
        model_gr = GridSearchCV(model, grid, scoring='recall', cv=5)
        model_gr.fit(x_train, y_train)

        model = model_gr.best_estimator_
    else:
        model.fit(x_train, y_train)

    return model


def predict_model(model: SklearnClassificationModel, x) -> np.ndarray:
    return model.predict(x)


def evaluate_model(y_pred: np.ndarray, y_target: np.ndarray) -> Dict[str, float]:
    return {'recall': recall_score(y_pred, y_target)}


def save_model(model: object, path2model: str):
    with open(path2model, 'wb') as f:
        pickle.dump(model, f)


def load_model(path2model: str):
    with open(path2model, 'rb') as f:
        model = pickle.load(f)
    return model
