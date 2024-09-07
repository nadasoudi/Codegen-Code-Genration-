import pandas as pd

df = pd.DataFrame({'Name': ['Rolf', 'Charlie', 'Anna', 'Bob', 'Jen', 'Sue'],
                   'Score': [85, 90, 95, 100, 95, 90]})

df.reset_index(inplace=True)

df.reset_index(inplace=True, drop=True)

df.reset_index(inplace=True, drop=True)

df.reset_index(inplace=True