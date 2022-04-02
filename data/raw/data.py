import pandas as pd
from config import Config

_db_config_path = r'C:\Users\WKS-ADM-binilyas\Documents\Python Scripts\myPro\data\db_config.ini'

def _extract_config():
    #Config().load_config(_db_config_path)
    config_params = Config()
    config_params.load_config(_db_config_path)

    global SQL_CONNECTION, SCHEMA_NAME, DATA_TABLE
    SQL_CONNECTION = config_params.get_config().get('trigger', 'SQL_CONNECTION')
    SCHEMA_NAME = config_params.get_config().get('trigger', 'SCHEMA_NAME')
    DATA_TABLE = config_params.get_config().get('trigger', 'DATA_TABLE')

def generate_query():
    query = f'SELECT * FROM {SCHEMA_NAME}.{DATA_TABLE}'
    return query

def extract_data():
    _extract_config()
    query = generate_query()
    df = pd.read_sql_query(query, SQL_CONNECTION)
    return df

if __name__ == '__main__':
    df = extract_data()
    print(df)