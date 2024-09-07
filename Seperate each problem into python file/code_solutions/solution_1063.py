import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(np.count_nonzero(a == b))

# Output:
# [10]
# [10]
# [10]