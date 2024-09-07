import pandas as pd

# Create a dataframe
df = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [5, 6, 7, 8]})

# Change the data type of col1
df['col1'] = df['col1'].astype('int64')

# Change the data type of col2
df['col2'] = df['col2'].astype('float64')