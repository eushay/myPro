# from raw_data import extract_data
from os import path
# import raw_data


# def test_data_extraction():
#    assert extract_data().empty == False
def test_db_path():
    assert path.exists(r'data/db_config.ini') == True
