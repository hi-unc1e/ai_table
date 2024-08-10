import pandas as pd

class SpreadsheetModel:
    def __init__(self):
        self.df = pd.DataFrame()

    def paste_data(self, clipboard_data):
        self.df = pd.read_csv(StringIO(clipboard_data), sep='\t')

    def get_cell_value(self, row, col):
        return self.df.iat[row, col]

    def set_cell_value(self, row, col, value):
        self.df.iat[row, col] = value
