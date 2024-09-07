import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

a[0, 1] = 5
a[1, 0] = 6

print(a)

# Output:
[[1 5]
 [4 6]]

"""

import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

a[0, 1] = 5
a[