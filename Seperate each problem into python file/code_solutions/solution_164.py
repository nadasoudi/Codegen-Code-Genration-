import numpy as np

matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print("Original matrix:")
print(matrix)

print("\nSubtracted mean:")
print(matrix - np.mean(matrix, axis=0))

# Output:
# [[1. 0. 0.]
#  [5. 6. 7.]