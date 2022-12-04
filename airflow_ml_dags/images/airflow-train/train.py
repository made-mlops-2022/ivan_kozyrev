import os
import pickle
import pandas as pd

import click
from sklearn.tree import DecisionTreeClassifier

TRAIN_X_DATA_FILE = "x_train.csv"
TRAIN_Y_DATA_FILE = "y_train.csv"


@click.command('train', context_settings={"ignore_unknown_options": True})
@click.option("--input-dir", type=click.Path())
@click.option("--output-dir", type=click.Path())
def train(input_dir: str, output_dir: str):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    x_train = pd.read_csv(os.path.join(input_dir, TRAIN_X_DATA_FILE))
    y_train = pd.read_csv(os.path.join(input_dir, TRAIN_Y_DATA_FILE))

    model = DecisionTreeClassifier(max_depth=10)
    model.fit(x_train, y_train)
    with open(os.path.join(output_dir, 'dectree_model.sav'), 'wb') as f:
        pickle.dump(model, f)


if __name__ == "__main__":
    train()
