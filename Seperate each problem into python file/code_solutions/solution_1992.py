>>> import numpy as np
>>> import numpy.linalg as la
>>>
>>> A = np.array([[1, 2, 3], [4, 5, 6]])
>>> B = np.array([[7, 8, 9], [10, 11, 12]])
>>> C = np.array([[13, 14, 15], [16, 17, 18]])
>>>
>>> print(la.KroneckerProduct(A, B))
[[1 2 3