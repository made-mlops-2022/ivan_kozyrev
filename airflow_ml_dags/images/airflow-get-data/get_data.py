import click
import os
import pandas as pd

from sdv.tabular import GaussianCopula

DATA_FILE_NAME = 'data4request.csv'


@click.command("get_data", context_settings={"ignore_unknown_options": True})
@click.option('--output-dir', type=click.Path(), required=True)
def get_data(output_dir: str):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    data = pd.read_csv(DATA_FILE_NAME)
    syn_model_data = GaussianCopula()
    syn_model_data.fit(data)
    syn_model_data.sample(200).to_csv(os.path.join(output_dir, DATA_FILE_NAME), index=False)



if __name__ == "__main__":
    get_data()
