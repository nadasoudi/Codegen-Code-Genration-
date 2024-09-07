import numpy as np

# Create a 2D NumPy array
arr = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20]])

# Calculate the mean across dimension in arr
print(arr.mean(axis=0))

# Calculate the mean across dimension in arr
print(arr.mean