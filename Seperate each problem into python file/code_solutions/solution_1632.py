import pandas as pd

df = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [10, 20, 30, 40, 50]})

df.dropna(axis=0, inplace=True)

df.dropna(axis=1, inplace=True)

df.dropna(axis=1, how='all')

df.dropna(axis=1,