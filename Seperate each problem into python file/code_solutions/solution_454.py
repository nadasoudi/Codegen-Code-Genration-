import pandas as pd

# Read the data from the file
df = pd.read_csv("data.csv")

# Extract the items at the given positions
print(df.iloc[:, 0:2])

# Extract the items at the given positions
print(df.iloc[:, 0:2, 2])

# Extract the items at the given positions
print(df.iloc[:, 0:2, 3])

# Extract the items at the given