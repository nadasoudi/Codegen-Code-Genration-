import numpy as np

# Create a matrix
A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

# Create a vector
b = np.array([1, 2, 3, 4])

# Solve the problem
x = np.linalg.solve(A, b)

# Print the solution
print(x)

# Create a matrix
A = np.array