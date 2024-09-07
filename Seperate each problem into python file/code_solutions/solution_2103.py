import pandas as pd

df = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [10, 20, 30, 40, 50]})

# Solution 1
df.iloc[:, 0] = df.iloc[:, 0].astype('int64')

# Solution 2
df.iat[0, 0] = df.iat[0, 0].astype('int64')

#