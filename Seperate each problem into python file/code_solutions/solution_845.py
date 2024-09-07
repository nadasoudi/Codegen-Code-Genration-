import pandas as pd
import numpy as np

# Read the data from the file
df = pd.read_csv("data.csv")

# Create a new dataframe with the columns
# "x" and "y"
df_new = pd.DataFrame(columns=["x", "y"])

# Create a new column "z"
df_new["z"] = df["x"] + df["