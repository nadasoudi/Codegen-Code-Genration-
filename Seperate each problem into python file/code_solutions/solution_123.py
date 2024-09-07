import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

arr_swapped = np.swapaxes(arr, 0, 1)

print(arr_swapped)

# Output:
[[1 4]
 [2 5]
 [3 6]
 [7 8]
 [4 9]]

# Task

# You are given an array of size N