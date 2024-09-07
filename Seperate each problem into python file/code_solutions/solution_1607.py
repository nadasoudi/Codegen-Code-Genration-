import pandas as pd

df = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [10, 20, 30, 40, 50]})

df.groupby('col1').size()

df.groupby('col1').size().sort_values(ascending=False)

df.groupby('col1').size().sort_values(ascending=False).head(