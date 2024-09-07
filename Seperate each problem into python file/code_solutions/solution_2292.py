def group_elements(matrix):
    # Write your code here
    if len(matrix) == 0:
        return []
    if len(matrix) == 1:
        return [matrix[0]]
    if len(matrix) == 2:
        return [matrix[0], matrix[1]]
    if len(matrix) == 3:
        return [matrix[0], matrix[1], matrix[2]]
    if len(matrix) == 4:
        return [mat