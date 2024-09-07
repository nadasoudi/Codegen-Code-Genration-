import numpy as np

arr = np.array([1, 2, 3, 4, 5])

np.save('arr.npy', arr)

arr = np.load('arr.npy')

arr

arr.shape

arr.size

arr.dtype

arr.ndim

arr.itemsize

arr.nbytes

arr.nbytes / arr.itemsize

arr.nbytes / arr.itemsize / arr.n