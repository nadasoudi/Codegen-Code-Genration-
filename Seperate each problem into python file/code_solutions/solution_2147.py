def solution(n, m, arr):
    # Write your code here
    # Create a dictionary to store the scores
    score = {}
    # Create a matrix to store the scores
    matrix = []
    # Create a matrix to store the scores
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(0)
    # Populate the matrix with the scores
    for i in range(n):
        for j in