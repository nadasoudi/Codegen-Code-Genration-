import pandas as pd

df = pd.DataFrame({'Name': ['Rolf', 'Bob', 'Jen', 'Anne'],
                   'Score': [60, 70, 80, 90]})

# Solution 1
print(df['Name'].count())

# Solution 2
print(df['Name'].value_counts())

# Solution 3
print(df['Name'].value_counts(sort=False))

# Solution