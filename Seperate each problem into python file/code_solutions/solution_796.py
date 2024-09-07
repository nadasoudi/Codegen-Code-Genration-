import numpy as np
import pandas as pd

# Create a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Create a Pandas series
series = pd.Series(arr)

# Print the array
print(arr)

# Print the series
print(series)

# Convert the array to a Pandas series
series = pd.Series(arr,