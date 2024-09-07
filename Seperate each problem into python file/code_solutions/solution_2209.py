import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")

# Create a new column in DataFrame called "min_value"
df["min_value"] = df["value"].transform(min)

# Print the DataFrame
print(df)

# Create a new column in DataFrame called "max_value"
df["max_value"] = df["value"].transform(max)

# Print the DataFrame
print(df