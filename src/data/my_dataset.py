import pandas as pd

from data.processed import process
from data import data_config


def get_x_y(df):
    x_columns = [c for c in df.columns if c not in [data_config.X_col_date, data_config.y_col_occupancy]]
    X = df[x_columns]
    y = df[data_config.y_col_occupancy]
    return X, y


def make_dataset():
    df = process.process_raw_data()
    df.drop('id', axis=1, inplace=True)
    #df[data_config.X_col_date] = pd.to_datetime(data_config.X_col_date)
    df.to_csv('processed_data.csv')
    return df


if __name__ == '__main__':
    df = make_dataset()
    X, y = get_x_y(df)
