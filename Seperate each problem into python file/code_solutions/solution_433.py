import pandas as pd

df = pd.DataFrame({'col1': ['a', 'b', 'c', 'd'], 'col2': ['A', 'B', 'C', 'D']})

print(df.loc[df['col1'].str.contains('A')])

# Output:
#     col1    col2
# 0    a    A
# 1    b    B
# 2