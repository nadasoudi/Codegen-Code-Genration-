import pandas as pd

df = pd.read_csv("world_alcohol_consumption.csv")

df = df[df['alcohol']!= '?']

df.to_csv('world_alcohol_consumption_filtered.csv')

# Solution:

df = pd.read_csv("world_alcohol_consumption_filtered.csv")

df = df[df['alcohol']!= '?']

df