import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print(a)

a[0, :] = 0
a[:, 0] = 0
a[:, :] = 0

print(a)

a[0, :] = 0
a[:, 0] = 0
a[:, :]