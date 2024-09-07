import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

a = np.insert(a, 2, [7, 8, 9], axis=1)

print(a)

# OUTPUT:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# a = np.array([[1, 2, 3], [4, 5, 6]])