import numpy as np

# Create a random matrix
matrix = np.random.randint(0, 10, size=(12, 12))

# Create a 4x4 block
block = np.zeros((4, 4))

# Fill the block with the values
for i in range(4):
    for j in range(4):
        block[i][j] = matrix[i][j]

# Print the block
print(