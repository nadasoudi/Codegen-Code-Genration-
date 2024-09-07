def reverse_every_kth_row(matrix, k):
    for i in range(k):
        for j in range(len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k = 2
print(reverse_every_kth_row(matrix