import numpy as np

def totest(x):
    if x > 0:
        return 1
    else:
        return -1

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(totest(x))

"""

# Solution

import numpy as np

def totest(x):
    if x > 0:
        return 1
    else:
        return -