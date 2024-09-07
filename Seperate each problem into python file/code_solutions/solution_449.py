import pandas as pd

df = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [1, 2, 3, 4, 5]})
print(df.isnull().sum())

# Solution:

# df = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [1, 2, 3, 4, 5]})
# print(df