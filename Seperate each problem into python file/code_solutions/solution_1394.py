def dimension(matrix):
    if len(matrix) == 0:
        return 0
    else:
        return len(matrix[0]) + dimension(matrix[1:])

print(dimension([[1,2,3],[4,5,6],[7,8,9]]))

"""

def dimension(matrix):
    if len(matrix) == 0:
        return 0
    else:
        return len(matrix[0]) + dimension(mat