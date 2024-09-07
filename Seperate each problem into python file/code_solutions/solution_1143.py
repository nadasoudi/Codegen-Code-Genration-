import pandas as pd

df = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [10, 20, 30, 40, 50]})

# drop rows where all elements are missing in the DataFrame
df.dropna(inplace=True)

# print the DataFrame
print(df)

# output
#     col1  col2
# 0     1     10
# 1