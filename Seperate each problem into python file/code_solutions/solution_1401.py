import pandas as pd

df = pd.read_excel('coalpublic2013.xlsx')

print(df['Production (short tons)'].sum())
print(df['Production (short tons)'].mean())
print(df['Production (short tons)'].max())
print(df['Production (short tons)'].min())

# Solution:

import pandas as pd