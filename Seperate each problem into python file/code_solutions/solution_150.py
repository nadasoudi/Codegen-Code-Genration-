import pandas as pd

# Create a dataframe
df = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [10, 20, 30, 40, 50]})

# Create a new column
df['col3'] = df['col1'] * 2

# Create a new column
df['col4'] = df['col2'] * 3

# Create a new column
df['col