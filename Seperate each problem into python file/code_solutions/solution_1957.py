import numpy as np

x = np.arange(0, 10, 0.1)
y = np.arange(0, 10, 0.1)

# Create a 2D grid
X, Y = np.meshgrid(x, y)

# Create a 2D array of coefficients
coefficients = np.array([[1, 2, 3], [4, 5, 6]])

# Create a 2D array of values
values = np.array([1,