import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)

weight = np.array([[1, 2, 3], [4, 5, 6]])
print(weight)

weighted_array = np.dot(weight, a)
print(weighted_array)

weighted_array = np.dot(weight, a, dtype=np.int64)
print(weighted_