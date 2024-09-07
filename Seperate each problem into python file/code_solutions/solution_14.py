import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

c = np.concatenate((a, b), axis=0)
print(c)

# Solution:

# a = np.array([1, 2, 3, 4