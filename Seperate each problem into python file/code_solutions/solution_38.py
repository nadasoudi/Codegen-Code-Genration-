import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a[:, 2])

# Output:
# [1 2 3]
# [4 5 6]
# [7 8 9]

# Hint: To solve this problem, you can use the numpy.ndarray.T method.
# For example, to access the transpose of a matrix, use np.