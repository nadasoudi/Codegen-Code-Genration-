import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

L = np.linalg.cholesky(A)

print(L)

# Output:
[[ 1.  2.  3.]
 [ 4.  5.  6.]
 [ 7.  8.  9.]]

"""

import numpy as