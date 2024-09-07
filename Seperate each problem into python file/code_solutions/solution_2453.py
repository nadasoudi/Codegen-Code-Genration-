def check_matrix(matrix1, matrix2):
    if len(matrix1)!= len(matrix2):
        return False
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            if matrix1[i][j]!= matrix2[i][j]:
                return False
    return True

print(check_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]