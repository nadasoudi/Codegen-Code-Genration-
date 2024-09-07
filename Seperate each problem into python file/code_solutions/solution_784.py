import pandas as pd

df = pd.DataFrame({'Name': ['Rolf', 'Charlie', 'Anna', 'Bob', 'Jen', 'Sue'],
                   'Score': [60, 70, 65, 60, 70, 90]})

# Solution 1
df.loc[df['Name'] == 'Rolf', 'Score'] = 100

# Solution 2
df.loc[df['Name'] == 'Charlie', 'Score'] = 100