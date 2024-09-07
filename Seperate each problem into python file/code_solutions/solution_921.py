def sort_matrix(matrix):
    rows = len(matrix)
    sum_rows = sum(matrix[0])
    for row in matrix:
        for i in range(len(row)):
            row[i] = row[i]/sum_rows
    return matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sort_matrix(matrix))