import pytest
from raw_data import extract_data

def test_data_extraction():
    assert extract_data().empty == False