import click
import pandas as pd
import os

FEATURES_FILE = "data.csv"
TARGET_FILE = "target.csv"


@click.command('preprocess', context_settings={"ignore_unknown_options": True})
@click.option("--input-dir", type=click.Path())
def preprocess(input_dir: str):
    data_features = pd.read_csv(os.path.join(input_dir, FEATURES_FILE))

    data_features.fillna(data_features.mean(numeric_only=True).round(1), inplace=True)

    data_features.to_csv(os.path.join(input_dir, FEATURES_FILE), index=False)


if __name__ == "__main__":
    preprocess()
