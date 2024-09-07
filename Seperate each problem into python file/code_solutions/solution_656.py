import pandas as pd

df = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [10, 20, 30, 40, 50]})
print(df)

# Solution:
df.loc[df['col1'] == 'M', 'col1'] = df['col2']
print(df)

# Solution:
df.loc[df['col1'] == 'M', ['col