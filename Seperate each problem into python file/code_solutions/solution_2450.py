def max_element(matrix):
    max_element = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > max_element:
                max_element = matrix[i][j]
    return max_element

print(max_element([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

"""

def max_element(matrix):
    max