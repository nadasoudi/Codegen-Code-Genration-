import pandas as pd

# Create a dataframe
df = pd.DataFrame({'day': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                   'intraday': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})

# Create a time series
ts = df.groupby('day').sum()

# Create a time series
ts = df.groupby('