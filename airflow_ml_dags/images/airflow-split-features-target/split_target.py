import click
import pandas as pd
import os

FEATURES_FILE = "data.csv"
TARGET_FILE = "target.csv"
DATA_FILE_NAME = 'data4request.csv'


@click.command('split_target', context_settings={"ignore_unknown_options": True})
@click.option("--input-dir", type=click.Path())
@click.option("--target-colm", type=str, default=-1, required=False)
def split_target(input_dir: str, target_colm: str):
    data = pd.read_csv(os.path.join(input_dir, DATA_FILE_NAME))

    if target_colm == -1:
        target_colm = data.columns[-1]

    features = data.drop(columns=[target_colm], axis=1)
    target = data[target_colm]

    features.to_csv(os.path.join(input_dir, FEATURES_FILE), index=False)
    target.to_csv(os.path.join(input_dir, TARGET_FILE), index=False)
    os.remove(os.path.join(input_dir, DATA_FILE_NAME))


if __name__ == "__main__":
    split_target()
