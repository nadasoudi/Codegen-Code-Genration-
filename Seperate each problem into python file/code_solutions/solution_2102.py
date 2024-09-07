import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Save the NumPy array as a text file
np.savetxt('arr.txt', arr)

# Load the NumPy array as a text file
arr = np.loadtxt('arr.txt')

# Print the NumPy array
print(arr)

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5