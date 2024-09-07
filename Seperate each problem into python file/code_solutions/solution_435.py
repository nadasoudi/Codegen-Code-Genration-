import pandas as pd

df = pd.read_csv("world_alcohol_consumption.csv")

df = df[df['region'].str.contains('Ea')]

df.to_csv('world_alcohol_consumption_filtered.csv', index=False)

# Solution:

# df = pd.read_csv("world_alcohol_consumption_filtered.csv")
# df