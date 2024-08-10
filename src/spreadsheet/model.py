from io import StringIO

import pandas as pd

class SpreadsheetModel:
    def __init__(self):
        self.df = pd.DataFrame()
        self.df = pd.read_csv("/Users/dpdu/Desktop/opt/spreadsheet_ai_app/index.csv", sep='\t')

    def paste_data(self, data):
        self.df = pd.read_csv(StringIO(data), sep='\t')

    def get_cell_value(self, row, col):
        return self.df.iat[row, col]


    def set_cell_value(self, row, col, value):
        column_name = self.df.columns[col]
        self.df.at[row, column_name] = value

