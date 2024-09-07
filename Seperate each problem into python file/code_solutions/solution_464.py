import pandas as pd

# Create a dataframe
df = pd.DataFrame({'Name': ['Alisa', 'Bethany', 'Cathrine', 'Evelyn'],
                   'Age': [21, 32, 23, 33],
                   'Score': [76, 65, 56, 78]})

# Create a series
s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])