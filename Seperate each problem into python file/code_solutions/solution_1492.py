import pandas as pd
import numpy as np

# Read the data
df = pd.read_csv("data.csv")

# Create a new dataframe with the new column
df_new = df.copy()

# Create a new column with the new column
df_new["smaller_value"] = df["smaller_value"].apply(lambda x: x if x < x else x - 1)

# Create