import numpy as np

def euclidean_distance(x, y):
    return np.sqrt(np.sum((x - y) ** 2))

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 3, 4, 5])

print(euclidean_distance(x, y))

"""

# Solution:

import numpy as np

def euclidean_distance(x