import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(A)

print(A.sum())

print(A.mean())

print(A.max())

print(A.min())

print(A.transpose())

print(A.dot(A))

print(A.dot(A, axis=0))

print(A.dot(A, axis=