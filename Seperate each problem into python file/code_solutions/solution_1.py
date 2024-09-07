import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(a)

a = np.repeat(a, 2)

print(a)

a = np.repeat(a, 2, axis=0)

print(a)

a = np.repeat(a, 2, axis=1)

print(a)

a = np.repeat(a, 2, axis=