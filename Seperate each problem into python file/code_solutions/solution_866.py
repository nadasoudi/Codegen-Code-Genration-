import pandas as pd

# Read the data
df = pd.read_csv("data/missing_values.csv")

# Print the number of missing values
print(df.isnull().sum())

# Print the number of missing values
print(df.isnull().sum().sum())

# Print the number of missing values
print(df.isnull().sum().sum())

# Print the number of missing values
print(df.