import pandas as pd
from data.raw import raw_data

class Process_data():

    def __init__(self):
        df = None

    def read_data(self):
        self.df = raw_data.extract_data()
        return self.df

    def delete_dups(self):
        self.df.drop_duplicates(keep='first', inplace=True)
        return self.df

    def set_index(self, col: str):
        self.df.set_index(col, inplace=True)
        return self.df

    def get_columns(self):
        return self.df.columns
