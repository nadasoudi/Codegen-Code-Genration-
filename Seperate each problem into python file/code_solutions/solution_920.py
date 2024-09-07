import pandas as pd

df = pd.read_csv('world_alcohol_consumption.csv')

df = df[df['region'].isin(['Africa', 'Eastern Mediterranean', 'Europe'])]

df.to_csv('world_alcohol_consumption_filtered.csv', index=False)

# Solution:

# df = pd.read_csv('world_alcohol