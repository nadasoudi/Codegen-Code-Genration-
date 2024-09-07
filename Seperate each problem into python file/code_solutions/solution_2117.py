import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

print(a)
print(b)

print(a.dot(b))
print(a.dot(b, axis=0))
print(a.dot(b, axis=1))

print(a.T)
print(a.T.dot(b))
print