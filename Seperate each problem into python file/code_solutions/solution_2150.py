import pandas as pd

df = pd.DataFrame({'col1': [1, 2, 3, 4, 5],
                   'col2': [10, 20, 30, 40, 50]})

# 1. Create a boolean column named 'is_even'
df['is_even'] = df['col1'] % 2 == 0

# 2. Print the dataframe
print(df)

# 3. Print the boolean column
print(df['is_even'])

#