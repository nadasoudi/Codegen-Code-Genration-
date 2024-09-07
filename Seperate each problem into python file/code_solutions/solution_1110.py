import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
a[0][0] = -1
print(a)

# Output:
[[-1 -1 -1]
 [ 0  0  0]
 [ 1  1  1]]

"""

import numpy as np

a = np.array([[1, 2, 3],