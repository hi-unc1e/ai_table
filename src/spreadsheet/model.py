from io import StringIO

import pandas as pd

from config.settings import default_csv_cache


class SpreadsheetModel:
    def __init__(self):
        self.df = pd.DataFrame()
        self.df = pd.read_csv(default_csv_cache, sep='\t')

    def paste_data(self, data):
        self.df = pd.read_csv(StringIO(data), sep='\t')

    def get_cell_value(self, row, col):
        return self.df.iat[row, col]


    def set_cell_value(self, row, col, value):
        column_name = self.df.columns[col]
        self.df.at[row, column_name] = value

