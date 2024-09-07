import numpy as np

a = np.array([1, 2, 3, 4, 5])

rounded = np.around(a)

rounded[rounded == 5] = 5

rounded[rounded == 4] = 3

rounded[rounded == 3] = 2

rounded[rounded == 2] = 1

rounded[rounded == 1] = 0

print(rounded)

"""

# Solution

import numpy as np

a = np.array([1,