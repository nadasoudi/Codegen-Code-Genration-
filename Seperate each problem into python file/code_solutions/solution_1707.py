def matrix_to_dict(matrix):
    dictionary = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            dictionary[matrix[i][j]] = matrix[i][j]
    return dictionary

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix_to_dict(matrix))

"""

def matrix_to_dict(mat