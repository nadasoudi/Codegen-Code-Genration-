import pandas as pd

# Create a Pandas DataFrame
df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})

# Add the new column to the existing DataFrame
df['col3'] = df['col1'] + df['col2']

# Print the new DataFrame
print(df)

# Create a Pandas Series
s = pd.Series([1, 2, 3, 4