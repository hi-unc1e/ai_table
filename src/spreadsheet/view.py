import tkinter as tk
from tkinter import ttk

class SpreadsheetView:
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Spreadsheet AI App")
        
       # 创建表格
        self.tree = ttk.Treeview(self.root, columns=range(controller.model.df.shape[1]), show='headings')
        for col in controller.model.df.columns:
            self.tree.heading(col, text=col)
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


    def update_data(self):
        try:
            self.load_data()
        except Exception as e:
            tk.messagebox.showerror("Error", str(e))

    def save_data(self, column, row, entry):
        # 保存编辑后的数据到DataFrame
        value = entry.get()
        self.controller.model.set_cell_value(int(row) - 1, column, value)
        self.load_data()  # 更新视图

        # 销毁编辑框
        entry.destroy()


    def on_double_click(self, event):
        # 获取当前单元格的位置
        item_id = self.tree.focus()
        column = self.tree.identify_column(event.x)
        row = self.tree.item(item_id, "text")

        # 创建一个编辑框
        entry = tk.Entry(self.root)
        entry.place(x=event.x, y=event.y, width=50, height=20)

        # 当编辑框失去焦点时，保存数据并销毁编辑框
        entry.bind("<Return>", lambda e, col=column, row=row, entry=entry: self.save_data(col, row, entry))
        entry.bind("<FocusOut>", lambda e, col=column, row=row, entry=entry: self.save_data(col, row, entry))
        entry.focus_set()


    def run(self):
        # 定期更新数据
        self.root.after(1000, self.update_data)  
        self.root.mainloop()
