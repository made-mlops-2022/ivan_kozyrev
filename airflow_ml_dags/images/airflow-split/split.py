import click
import pandas as pd
import os

from sklearn.model_selection import train_test_split

FEATURES_FILE = "data.csv"
TARGET_FILE = "target.csv"


@click.command('split', context_settings={"ignore_unknown_options": True})
@click.option('--input-dir', type=click.Path())
@click.option('--output-dir', type=click.Path())
@click.option('--coef-split', type=float, required=False, default=0.2)
def split(input_dir: str, output_dir: str, coef_split: float):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    x_data = pd.read_csv(os.path.join(input_dir, FEATURES_FILE))
    y_data = pd.read_csv(os.path.join(input_dir, TARGET_FILE))

    x_train, x_val, y_train, y_val = train_test_split(x_data, y_data, test_size=coef_split)
    x_train.to_csv(os.path.join(output_dir, "x_train.csv"), index=False)
    x_val.to_csv(os.path.join(output_dir, "x_val.csv"), index=False)
    y_train.to_csv(os.path.join(output_dir, "y_train.csv"), index=False)
    y_val.to_csv(os.path.join(output_dir, "y_val.csv"), index=False)


if __name__ == "__main__":
    split()
