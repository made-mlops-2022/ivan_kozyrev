import os
import pickle
import click
import pandas as pd

TRAIN_X_DATA_FILE = "data.csv"
MODEl_FILE = "dectree_model.sav"


@click.command('predict', context_settings={"ignore_unknown_options": True})
@click.option('--input-dir', type=click.Path())
@click.option('--output-dir', type=click.Path())
@click.option('--model-dir', type=click.Path())
def predict(input_dir: str, output_dir: str, model_dir: str):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    x_train = pd.read_csv(os.path.join(input_dir, TRAIN_X_DATA_FILE))

    all_subdirs = [os.path.join(model_dir, d) for d in os.listdir(model_dir) if
                   os.path.isdir(os.path.join(model_dir, d))]
    latest_subdir = max(all_subdirs, key=os.path.getmtime)
    with open(os.path.join(latest_subdir, MODEl_FILE), "rb") as f:
        model = pickle.load(f)

    pred = model.predict(x_train)
    pd.DataFrame(pred).to_csv(os.path.join(output_dir, 'predict.csv'), index=False)


if __name__ == "__main__":
    predict()
