import pandas as pd

# Create a dataframe
df = pd.DataFrame({'year': [2015, 2016, 2017, 2018],
                   'day': [5, 6, 7, 8]})

# Create a new column
df['year_day'] = df['year'] * 24 + df['day']

# Create a new column
df['year_day'] = df['year_day'].astype('Int64')