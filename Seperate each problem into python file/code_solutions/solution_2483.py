def is_symmetric(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]!= matrix[j][i]:
                return False
    return True

print(is_symmetric([[1,2,3],[4,5,6],[7,8,9]]))
print(is_symmetric([[1,2,3],[4,5,6],[7,8