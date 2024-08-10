import tkinter


def get_clipboard_data():
    root = tkinter.Tk()
    root.withdraw()  # 隐藏主窗口
    clipboard_data = root.clipboard_get()
    root.destroy()
    return clipboard_data