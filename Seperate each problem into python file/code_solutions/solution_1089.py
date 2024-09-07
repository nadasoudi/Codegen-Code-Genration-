import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x.shape = (3, 2)

x[1, 1] = 0

print(x)

x.shape = (3, 2)

x[1, 1] = 0

print(x)

x.shape = (3, 2)

x[1, 1] = 0