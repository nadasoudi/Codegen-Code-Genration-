import numpy as np

x = np.arange(0, 10, 0.1)
y = np.arange(0, 10, 0.1)
z = np.arange(0, 10, 0.1)

X, Y, Z = np.meshgrid(x, y, z)

# print(X)
# print(Y)
# print(Z)

# print(np.polygrid3d(X, Y, Z))