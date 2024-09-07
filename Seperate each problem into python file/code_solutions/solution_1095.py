def remove_column(nested_list, column):
    """
    :type nested_list: List[List[int]]
    :type column: int
    :rtype: List[List[int]]
    """
    if column == 0:
        return nested_list
    else:
        return [item for item in nested_list if item is not None]

# Main
nested_list = [[1, 2, 3], [4, 5, 6], [7,