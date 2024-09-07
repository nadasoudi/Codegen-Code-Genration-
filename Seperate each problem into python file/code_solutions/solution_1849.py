import numpy as np

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

a.shape = (3, 4)

a.dtype = 'int64'

a.sum()

a.sum(axis=0)

a.sum(axis=1)

a.sum(axis=1, dtype='int64')