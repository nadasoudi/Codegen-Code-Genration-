import pandas as pd

df = pd.DataFrame({'Name': ['Rolf', 'Charlie', 'Anna', 'Bob', 'Jen', 'Sue'],
                   'Age': [30, 32, 33, 34, 35, 36],
                   'Score': [85, 90, 95, 100, 90, 100]})

df.groupby('Name').count()

df.groupby('Name').sum()

df.