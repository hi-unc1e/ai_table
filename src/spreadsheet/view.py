import tkinter as tk
from tkinter import ttk

class SpreadsheetView:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Spreadsheet AI App")

        # 创建表格
        cols = list(controller.model.df.columns)
        self.tree = ttk.Treeview(self.root, columns=cols, show='headings')
        for col in controller.model.df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)  # 设置默认列宽
        self.tree.pack(expand=True, fill='both')

        # 双击单元格时编辑
        self.tree.bind("<Double-1>", self.on_double_click)

        # 初始化表格数据
        self.load_data()

    def load_data(self):
        # 清除现有数据
        for i in self.tree.get_children():
            self.tree.delete(i)

        # 加载数据到表格
        for index, row in self.controller.model.df.iterrows():
            self.tree.insert('', 'end', values=list(row))

    def save_data(self, column, row, entry):
        value = entry.get()
        row = int(self.tree.index(self.tree.selection()[0]))
        col_index = int(column[1:]) - 1
        self.controller.model.set_cell_value(row, col_index, value)  # 使用整数行号
        self.load_data()  # 更新视图

        # 销毁编辑框
        entry.destroy()

    def on_double_click(self, event):
        # 获取当前单元格的位置
        item_id = self.tree.focus()
        column_index = int(self.tree.identify_column(event.x)[1:]) - 1
        row_index = int(self.tree.identify_row(event.y)[1:]) - 1
        col_name = self.controller.model.df.columns[column_index]

        # 获取单元格值
        cell_value = self.controller.model.get_cell_value(row_index, column_index)

        # 创建一个编辑框
        entry = tk.Entry(self.root)
        entry.insert(0, cell_value)
        entry.place(x=event.x, y=event.y)

        # 当编辑框失去焦点时，保存数据并销毁编辑框
        entry.bind("<Return>", lambda e: self.save_data(col_name, row_index, entry))
        entry.bind("<FocusOut>", lambda e: self.save_data(col_name, row_index, entry))
        entry.focus_set()

    def run(self):
        self.root.mainloop()