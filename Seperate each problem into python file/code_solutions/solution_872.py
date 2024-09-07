import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([2, 3, 4, 5, 6])

print(np.set_exclusive_zeros(a, b))

# OUTPUT:
# [1 2 3 4 5 6 5 6 6]
# [2 3 4 5 6 6 6