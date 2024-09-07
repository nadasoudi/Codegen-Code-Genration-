import pandas as pd

df = pd.DataFrame({'col1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                   'col2': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                   'col3': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})

print(df.groupby(['col1', '