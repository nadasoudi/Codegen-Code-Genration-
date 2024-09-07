import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [10, 11, 12]])

inner = A.dot(B)
outer = A.dot(B, transpose=True)
cross = A.dot(B, transpose=False)

print("inner:", inner)
print("outer:", outer)
print("