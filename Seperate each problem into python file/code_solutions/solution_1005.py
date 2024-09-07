import numpy as np

# Create an array of random numbers
np.random.seed(0)
a = np.random.randint(10, size=(5, 5))
print(a)

# Find the minimum and maximum values
print(np.min(a))
print(np.max(a))

# Create a new array with random numbers
np.random.seed(0)
b = np.random.randint(10,