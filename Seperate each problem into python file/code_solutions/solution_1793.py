def matrix_to_string(matrix):
    # your code goes here
    return matrix

# driver code
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix_to_string(matrix))

# solution
def matrix_to_string(matrix):
    # your code goes here
    return '\n'.join([' '.join(map(str, row)) for row in matrix])

# driver code
mat