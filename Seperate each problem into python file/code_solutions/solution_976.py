import pandas as pd

df = pd.DataFrame({'col1': [1, 2, 3, 4, 5],
                   'col2': [10, 20, 30, 40, 50],
                   'col3': [100, 200, 300, 400, 500]})

df.dropna(subset=['col2'])

df.dropna(subset=['col3'])

df.dropna(subset