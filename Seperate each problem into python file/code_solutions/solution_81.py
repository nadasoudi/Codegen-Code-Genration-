import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# vertical split
arr = arr.reshape(3, 4)

# horizontal split
arr = arr.reshape(4, 3)

# vertical split
arr = arr.reshape(3, 4)

# horizontal split
arr = arr.reshape(