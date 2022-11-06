from typing import Tuple

import pandas as pd
import numpy as np

# def download_data_from_s3(s3_bucket: str, s3_path: str, output: str) -> NoReturn:
#     s3 = client("s3")
#     s3.download_file(s3_bucket, s3_path, output)
from sklearn.model_selection import train_test_split

from ml_project.src.customdataclasses import ModelParam


def read_data(path: str) -> pd.DataFrame:
    data = pd.read_csv(path)
    return data


def split_feature_target(data: pd.DataFrame, target_name: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    features_data = data.drop(columns=target_name)
    target_data = data[target_name].to_numpy()
    return features_data, target_data


def split_train_test_data(x: pd.DataFrame, y: pd.DataFrame, conf: ModelParam) -> Tuple[
    np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=conf.test_size, random_state=conf.random_state
    )
    return x_train, x_test, y_train, y_test
