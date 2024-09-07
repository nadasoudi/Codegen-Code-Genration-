import pandas as pd

# Read the data
df = pd.read_csv("https://github.com/datasets/csv/raw/master/data/fraud.csv")

# Create a new DataFrame with the missing values
df_new = df.copy()

# Replace the missing values with the interpolated value
df_new.fillna(value=df_new.interpolate().interpolate().interpolate