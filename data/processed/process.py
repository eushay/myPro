import pandas as pd
from data.processed.read_clean_data import ProcessData
from data import data_config


def process_raw_data() -> pd.DataFrame:
    processed_data = ProcessData()
    df = processed_data.read_data()
    df = processed_data.delete_dups()
    df = processed_data.set_index(data_config.X_col_date)
    return df


if __name__ == '__main__':
    df = process_raw_data()
