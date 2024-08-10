from src.spreadsheet.controller import SpreadsheetController


def test_main():
    controller = SpreadsheetController()
    controller.paste_from_clipboard()
    # 示例：计算A1 + B1
    result = controller.calculate_custom_function('custom_sum', 'A', 1, 'B', 1)
    print(f"The result of A1 + B1 is: {result}")


def main():
    print("on")
    controller = SpreadsheetController()
    controller.paste_from_clipboard()
    controller.show_view()  # 显示图形化界面
    print("and on")



if __name__ == "__main__":
    main()

