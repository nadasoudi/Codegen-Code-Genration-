import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

a.swapaxes(0, 1)
b.swapaxes(0, 1)

a.swapaxes(1, 2)
b.swapaxes(1, 2)

a.swapaxes(2, 0)
b.sw