def custom_sum(model, col1, row1, col2, row2):
    value1 = model.get_cell_value(row1 - 1, col1 - 1)
    value2 = model.get_cell_value(row2 - 1, col2 - 1)
    return value1 + value2
