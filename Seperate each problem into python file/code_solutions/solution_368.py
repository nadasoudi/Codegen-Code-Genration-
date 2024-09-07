import numpy as np

# Create a checkerboard matrix
checkerboard = np.zeros((8, 8), dtype=int)

# Fill the checkerboard matrix with pattern
for i in range(8):
    for j in range(8):
        if i % 2 == 0 and j % 2 == 0:
            checkerboard[i][j] = 1
        elif i % 2 == 0 and j % 2!= 0: