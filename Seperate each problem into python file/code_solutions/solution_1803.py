def count_row_length(matrix):
    count = 0
    for i in range(len(matrix)):
        count += len(matrix[i])
    return count

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(count_row_length(matrix))

"""

def count_row_length(matrix):
    count = 0
    for i in range(len(matrix)):