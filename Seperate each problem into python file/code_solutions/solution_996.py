import pandas as pd

df = pd.read_excel('coalpublic2013.xlsx')
df['Mine Name'] = df['Mine Name'].str.startswith('P')

print(df)

# Solution:

# df = pd.read_excel('coalpublic2013.xlsx')
# df['Mine Name'] = df['Mine Name'