import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(arr.sum())
print(arr.sum(axis=0))
print(arr.sum(axis=1))
print(arr.sum(axis=1).reshape(3, 2))

"""

import numpy as np

arr