import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(arr.nlargest(3))

# Output:
# [10, 9, 8]

# Hint:
# Use np.argsort() to get the indices of the elements in the array.
# Use np.sort() to sort the array in ascending order.
# Use np.argsort() to get the indices of the