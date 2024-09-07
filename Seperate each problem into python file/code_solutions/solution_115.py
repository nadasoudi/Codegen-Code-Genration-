import pandas as pd

# Read the data into a pandas DataFrame: df
df = pd.read_csv('titanic.csv')

# Print the head of the DataFrame
print(df.head())

# Print the column labels of the DataFrame
print(df.columns)

# Print the shape of the DataFrame
print(df.shape)

# Print the data types of the DataFrame
print