import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

print(np.median(arr))

# Output:
# [5.5 6.5 8.5]

# Hint:
# Use np.median() to compute the median of flattened given array.
# Use np.mean() to compute the mean of flattened given array.