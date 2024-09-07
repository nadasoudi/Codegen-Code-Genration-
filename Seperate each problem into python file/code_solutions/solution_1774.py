import numpy as np

A = np.random.randn(3,3)
B = np.random.randn(3,3)

print(A+B)
print(A-B)
print(A*B)
print(A/B)
print(A.dot(B))
print(A.T.dot(B))
print(A.T.dot(A))
print(A.T.dot(A.T))
print(A.T.dot(A