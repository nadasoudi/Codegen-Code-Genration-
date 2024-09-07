import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

print(a)
print(b)

a[0, 1] = b[1, 0]
a[0, 2] = b[1, 1]
a[1, 0] = b[2, 0]
a[1, 1] = b[