import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([2, 4, 6, 8, 10])

print(np.intersect1d(a, b))

# Output:
# [1, 2, 3, 4, 5]
# [2, 4, 6, 8, 10]

# Hint:
# Use np.intersect1d() to find the common values between two arrays.
# Use