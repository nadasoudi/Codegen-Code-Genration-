import pandas as pd

# Create a dataframe from the given data
df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [1, 2, 3, 4, 5], "C": [1, 2, 3, 4, 5]})

# Create a new column called "mean"
df["mean"] = df["A"].mean()

# Create a new column called "std"
df["