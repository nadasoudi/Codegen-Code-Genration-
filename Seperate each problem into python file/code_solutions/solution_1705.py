import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Print the indices of the array
print(arr.argsort())

# Print the indices of the array
print(arr.argsort(kind='mergesort'))

# Print the indices of the array
print(arr.argsort(kind='quicksort'))

# Print the indices of the array
print(arr.argsort