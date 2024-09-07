import numpy as np

array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
array2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(set(array1) - set(array2))

# Output: [1, 2, 3, 4, 5,