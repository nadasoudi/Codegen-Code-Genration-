import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[7, 8, 9], [10, 11, 12]])

print(np.where(x > 5))

# Output:
# [[1 3]
#  [4 5]]

print(np.where(x > 5, y, x))

# Output:
# [[1 2 3]
#  [4 5 6]]

print(np