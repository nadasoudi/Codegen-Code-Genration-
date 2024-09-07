import numpy as np

# Create a random matrix of cartesian coordinates
x = np.random.rand(10, 2)

# Convert the matrix to polar coordinates
polar = np.dot(x, np.array([[np.cos(x[i, 0]), np.sin(x[i, 0])] for i in range(10)]))

# Convert polar coordinates to cartesian coordinates
cartesian = np.dot(polar