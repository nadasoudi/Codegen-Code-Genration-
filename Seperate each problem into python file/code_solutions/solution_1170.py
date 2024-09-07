import pandas as pd

# Create a dataframe
df = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [10, 20, 30, 40, 50]})

# Create a series
s = pd.Series([1, 2, 3, 4, 5])

# Select a specific row
print(df.iloc[0])

# Select a specific row
print(df.il