import os
import pandas as pd
import click
import json
import pickle
from sklearn.metrics import accuracy_score, f1_score

MODEl_FILE = "dectree_model.sav"


@click.command('validate', context_settings={"ignore_unknown_options": True})
@click.option('--input-dir', type=click.Path())
@click.option('--output-dir', type=click.Path())
@click.option('--model-dir', type=click.Path())
def validate(input_dir: str, output_dir: str, model_dir: str):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(os.path.join(model_dir, MODEl_FILE), "rb") as f:
        model = pickle.load(f)

    x_val = pd.read_csv(os.path.join(input_dir, 'x_val.csv'))
    y_val = pd.read_csv(os.path.join(input_dir, 'y_val.csv'))
    predict = model.predict(x_val)

    accuracy = accuracy_score(y_val, predict)
    f1 = f1_score(y_val, predict, average='macro')

    metric_dict = {
        'accuracy': accuracy,
        'f1': f1,
    }

    with open(os.path.join(output_dir, 'valid_metric.json'), 'w') as f:
        json.dump(metric_dict, f)


if __name__ == "__main__":
    validate()
