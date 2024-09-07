import pandas as pd

df = pd.DataFrame({'col1': ['a', 'b', 'c', 'd'],
                   'col2': ['e', 'f', 'g', 'h'],
                   'col3': ['i', 'j', 'k', 'l']})

df.columns = ['col1', 'col2', 'col3']

print(df.head())

df.columns = ['col