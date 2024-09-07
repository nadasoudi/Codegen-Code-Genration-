import pandas as pd

df = pd.DataFrame({'col1': [1, 2, 3, 4, 5],
                   'col2': [10, 20, 30, 40, 50]})

df.index = ['a', 'b', 'c', 'd', 'e']

print(df)

# Solution:

# df = pd.DataFrame({'col1': [1, 2, 3, 4, 5],
#                   'col2': [10, 20