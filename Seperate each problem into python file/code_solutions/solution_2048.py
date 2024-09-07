import pandas as pd

# Read all CSV files in a folder in Pandas in Python
df = pd.read_csv('/Users/srinivasan/Desktop/Python/data/data.csv')

# Print the first 5 rows of the dataframe
print(df.head())

# Print the last 5 rows of the dataframe
print(df.tail())

# Print the number of rows in the dataframe
print(df.shape)

# Print the number of columns