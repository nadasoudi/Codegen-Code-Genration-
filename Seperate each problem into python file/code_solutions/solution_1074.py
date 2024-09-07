def sort_matrix(matrix):
    rows = len(matrix)
    sum_rows = sum(rows)
    for i in range(rows):
        for j in range(i+1, rows):
            if matrix[i][j] == 0:
                continue
            if matrix[i][j] < 0:
                matrix[i][j] = -matrix[i][j]
            else:
                matrix[i