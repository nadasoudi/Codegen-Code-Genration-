def extract_column(nested_list, column):
    """
    :param nested_list: nested list
    :param column: column to extract
    :return: list of values
    """
    return [value for row in nested_list for value in row[column]]

# driver code
nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(extract_column(