import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Compute the negative value of all elements in a NumPy array
np.negative(a)

# Compute the negative value of all elements in a NumPy array
np.negative(a, out=a)

# Compute the negative value of all elements in a NumPy array
np.negative(a, out=a, where