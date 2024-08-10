from src.utils.clipboard import get_clipboard_data
from src.spreadsheet.model import SpreadsheetModel
from src.ai.ai_functions import custom_sum
from src.spreadsheet.view import SpreadsheetView


class SpreadsheetController:
    def __init__(self):
        self.model = SpreadsheetModel()

    def paste_from_clipboard(self):
        data = get_clipboard_data()
        self.model.paste_data(data)

    def calculate_custom_function(self, func, *args):
        if func == 'custom_sum':
            return custom_sum(self.model, *args)
        # 其他自定义函数可以在这里添加

    def show_view(self):
        self.view = SpreadsheetView(self)
        self.view.run()