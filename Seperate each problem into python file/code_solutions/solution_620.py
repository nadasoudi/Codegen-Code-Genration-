import pandas as pd

df1 = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [5, 6, 7, 8]})
df2 = pd.DataFrame({'col1': [1, 2, 3, 4], 'col3': [5, 6, 7, 8]})

df1.fillna(df2)

df1.fill