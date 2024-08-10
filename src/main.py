import tkinter as tk
from io import StringIO
from tkinter import ttk
import pandas as pd

from config.settings import default_csv_cache


class SpreadsheetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Spreadsheet App")

        # 初始化 DataFrame
        COL_SIZE = 5
        LINE_SIZE = 40
        self.df = pd.DataFrame('', index=range(LINE_SIZE), columns=[chr(65 + i) for i in range(COL_SIZE)])  # A-J 十列, 40 行

        # 创建包含滚动条的Frame
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill='both')

        # 创建Treeview
        self.tree = ttk.Treeview(root, columns=self.df.columns, show='headings')
        self.tree.bind("<Double-1>", self.on_double_click)

        for index, col in enumerate(self.df.columns):
            self.tree.heading(index, text=col)
            self.tree.column(index, width=100)

        # 创建滚动条
        vsb = ttk.Scrollbar(frame, orient='vertical', command=self.tree.yview)
        vsb.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=vsb.set)

        self.tree.pack(expand=True, fill='both')

        self.load_data()

        # 添加入数据的Entry和Button
        self.entry_frame = tk.Frame(root)
        self.entry_frame.pack()

        self.entries = []
        for col in self.df.columns:
            entry = tk.Entry(self.entry_frame)
            entry.pack(side=tk.LEFT)
            self.entries.append(entry)

        # add 按钮
        self.add_button = tk.Button(self.entry_frame, text="Add Row", command=self.add_row)
        self.add_button.pack(side=tk.LEFT)

        # 添加保存按钮
        self.save_button = tk.Button(self.entry_frame, text="Save to CSV", command=self.save_to_csv)
        self.save_button.pack(side=tk.LEFT)

        # 添加粘贴按钮
        self.paste_button = tk.Button(self.entry_frame, text="Paste", command=self.paste_data)
        self.paste_button.pack(side=tk.LEFT)

    def load_data(self):
        # 清除现有数据
        for i in self.tree.get_children():
            self.tree.delete(i)

        # 加载数据到表格
        for index, row in self.df.iterrows():
            self.tree.insert('', 'end', values=list(row))

    def paste_data(self):
        try:
            # 从剪贴板获取数据
            clipboard_data = self.root.clipboard_get()
            # 将剪贴板数据转换为DataFrame
            data = pd.read_csv(StringIO(clipboard_data), sep='\t')
            # 更新DataFrame
            self.df = data
            # 重新加载数据
            self.load_data()
            print("Data pasted from clipboard")
        except Exception as e:
            print(f"Error pasting data: {e}")

    def add_row(self):
        new_row = {col: entry.get() for col, entry in zip(self.df.columns, self.entries)}
        self.df = self.df._append(new_row, ignore_index=True)
        self.load_data()

    def save_to_csv(self):
        self.df.to_csv(default_csv_cache, index=False)
        print("Data saved to index.csv")

    def save_data(self, col_index, row_index, entry):
        value = entry.get()
        self.df.iat[row_index, col_index] = value
        self.load_data()

        # 销毁编辑框
        entry.destroy()

    def on_double_click(self, event):
        # 获取当前单元格的位置
        item_id = self.tree.focus()

        # 获取列索引
        column = self.tree.identify_column(event.x)
        col_index = int(column.replace("#", "")) - 1

        # 获取行索引
        row_id = self.tree.identify_row(event.y)
        row_index = self.tree.index(row_id)

        # 获取单元格值
        cell_value = self.df.iat[row_index, col_index]

        # 创建一个编辑框
        entry = tk.Entry(self.root)
        entry.insert(0, cell_value)
        entry.place(x=event.x_root - self.root.winfo_rootx(),
                    y=event.y_root - self.root.winfo_rooty(), width=100)

        # 当编辑框失去焦点时，保存数据并销毁编辑框
        entry.bind("<Return>", lambda e: self.save_data(col_index, row_index, entry))
        entry.bind("<FocusOut>", lambda e: self.save_data(col_index, row_index, entry))
        entry.focus_set()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = SpreadsheetApp(root)
    app.run()
