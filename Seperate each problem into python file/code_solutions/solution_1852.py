def matrix_to_tuple(matrix):
    """Convert Matrix to tuple"""
    rows = len(matrix)
    if rows == 0:
        raise ValueError("matrix must have at least one row")
    cols = len(matrix[0])
    if cols == 0:
        raise ValueError("matrix must have at least one column")
    result = []
    for row in range(rows):
        result.append([])
        for col in range(cols