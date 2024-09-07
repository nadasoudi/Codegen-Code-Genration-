import pandas as pd

df = pd.DataFrame({'col1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                   'col2': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})

print(df['col2'].apply(len))

# Output:
# col2    8
# col1    10
# dtype: int