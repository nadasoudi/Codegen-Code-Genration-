def MatrixRowSubset(matrix, row, col):
    if row == len(matrix):
        return False
    if col == len(matrix[0]):
        return True
    if matrix[row][col] == 0:
        return False
    matrix[row][col] = 0
    return MatrixRowSubset(matrix, row + 1, col) or MatrixRowSubset(matrix, row, col + 1)

"""

def MatrixRowSubset(matrix, row, col