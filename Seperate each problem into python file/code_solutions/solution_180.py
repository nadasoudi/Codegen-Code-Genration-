import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

arr_space = np.insert(arr, 5,'')

print(arr_space)

# Output:
# [1 2 3 4 5 6 7 8 9 10]
# [1 2 3 4 5 6 7 8 9 10]
# [1 2 3 4 5 6 7 8 9 10]
#