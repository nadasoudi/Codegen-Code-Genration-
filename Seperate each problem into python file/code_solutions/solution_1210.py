import numpy as np

# Create an array filled with random floating point numbers with the specified precision
np.random.seed(123)
a = np.random.randn(10, 4)

# Set the array values with the specified precision
np.set_printoptions(precision=4)
print(a)

# Create a NumPy array filled with random floating point numbers with the specified precision
np.random.seed(