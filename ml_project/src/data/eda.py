import pandas as pd

from pandas_profiling import ProfileReport


def create_eda(path2csv: str, path2file: str):
    data = pd.read_csv(path2csv)
    profile = ProfileReport(data)
    profile.to_file(path2file)


if __name__ == "__main__":
    create_eda()
