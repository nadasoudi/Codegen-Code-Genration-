import pandas as pd

df = pd.DataFrame({'Name': ['Rolf', 'Charlie', 'Anna', 'Bob', 'Jen', 'Sue'],
                   'Score': [85, 90, 95, 100, 90, 100]})

df.head()

df.columns = ['Name', 'Score']
df.head()

df.columns = ['Name', 'Score']
df.head()

df.columns = ['Name', 'Score']