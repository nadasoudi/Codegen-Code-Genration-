import pandas as pd

# Read the data into a pandas dataframe
df = pd.read_csv("data.csv")

# Create a dictionary to group the data by two columns
grouped = df.groupby(['gender', 'age'])

# Create a dictionary to convert the data into a dictionary
converted = grouped.agg({"height": "mean", "weight": "mean"})