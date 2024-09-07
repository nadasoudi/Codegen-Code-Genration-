import pandas as pd

df = pd.DataFrame({'col1': ['a', 'b', 'c', 'd'], 'col2': ['e', 'f', 'g', 'h']})

print(df['col1'].str.lower().str.isupper())

# Output:
# True
# True
# True
# False

print(df['col1'].str.lower().str.