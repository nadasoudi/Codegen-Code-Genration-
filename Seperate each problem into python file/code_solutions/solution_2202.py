import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

Q, R = np.linalg.qr(A)

print(Q)
print(R)

# Output:
[[ 1.  2.  3.]
 [ 4.  5.  6.]
 [ 7.  8.  9.]]

[[ 1.  2.  3.]
 [