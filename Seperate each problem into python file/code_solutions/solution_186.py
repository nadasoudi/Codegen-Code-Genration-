import pandas as pd

# Read the data from the file
df = pd.read_csv("data.csv")

# Create a new column called "smallest"
df["smallest"] = df["smallest"].astype(str)

# Create a new column called "largest"
df["largest"] = df["largest"].astype(str)

# Create a new column called "smallest"
df["smallest