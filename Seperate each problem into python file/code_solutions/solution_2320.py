import numpy as np

n = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def filter_numpy(n):
    return n[n>5]

print(filter_numpy(n))

"""

# Solution

import numpy as np

n = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

def filter_numpy(n):