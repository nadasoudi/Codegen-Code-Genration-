import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                   'B': [10, 20, 30, 40, 50],
                   'C': ['a', 'b', 'c', 'd', 'e']})

# Create a MultiIndex
df.index = pd.MultiIndex.from_tuples([('A', 1), ('A