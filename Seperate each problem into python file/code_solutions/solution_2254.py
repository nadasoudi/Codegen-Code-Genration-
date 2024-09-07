def solve(n, m):
    matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = i + j
    for i in range(n):
        for j in range(n):
            if i % 2 == 0:
                matrix[i][j] = matrix[i][j]