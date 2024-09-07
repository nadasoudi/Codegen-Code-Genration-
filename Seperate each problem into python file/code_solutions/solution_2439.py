def is_identity(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]!= 0:
                return False
    return True

print(is_identity([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(is_identity([[1, 2, 3], [4, 5, 6], [7, 8, 9]]