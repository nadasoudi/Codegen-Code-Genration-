import numpy as np
import pandas as pd

# Read the data
data = pd.read_csv('data.csv')

# Replace NaN values with average of columns
data.fillna(data.mean(), inplace=True)

# Print the data
print(data)

# Create a new dataframe
new_data = data.copy()

# Replace NaN values with average of columns
new_data.fillna(new_data.mean(), inplace=True