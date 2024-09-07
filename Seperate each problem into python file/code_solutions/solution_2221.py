import numpy as np

d = {'a': 1, 'b': 2, 'c': 3}

np_array = np.array(d)

print(np_array)

# Output:
# array([1, 2, 3])

# Note:
# The order of the elements in the array is not important.
# The array is already in the correct order.
# The array is not a view of the original array.
# The array is not a copy of the original array.