def group_similar(matrix, n):
    # Write your code here
    matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i][j] = 1
            else:
                matrix[i][j] = matrix[i][j] + matrix[i][j-1]
    return matrix

matrix = [[1, 2, 3