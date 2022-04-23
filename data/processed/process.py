import pandas as pd
from read_clean_data import ProcessData
from utils.config import MyConfig

_data_config_path = r'data\data_config.ini'


def process_raw_data() -> pd.DataFrame:
    processed_data = ProcessData()
    df = processed_data.read_data()
    df = processed_data.delete_dups()
    config_parser = MyConfig()
    config_parser.load_config(_data_config_path)
    X_col_date = config_parser.get_config().get('columns', 'X_col_date')
    df = processed_data.set_index(X_col_date)
    return df


if __name__ == '__main__':
    df = process_raw_data()