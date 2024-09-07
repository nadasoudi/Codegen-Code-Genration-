import numpy as np

# Create a 4x4 matrix
matrix = np.zeros((4,4))

# Set the main diagonal to 1
matrix[0,0] = 1
matrix[0,1] = 1
matrix[0,2] = 1
matrix[0,3] = 1

# Set the main diagonal to 0
matrix[1,0] = 1
matrix[