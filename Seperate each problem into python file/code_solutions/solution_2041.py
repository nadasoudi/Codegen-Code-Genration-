import numpy as np

np.random.seed(42)

x = np.random.randn(3, 2)

print(x)

print(x.shape)

print(x.dtype)

print(x.size)

print(x.itemsize)

print(x.nbytes)

print(x.dtype)

print(x.nbytes / x.itemsize)

print(x.nbytes / x.itemsize)