import pandas as pd

df = pd.read_csv('world_alcohol_consumption.csv')

df.dropna(axis=0, inplace=True)

df.dropna(axis=1, inplace=True)

df.dropna(how='any', inplace=True)

df.dropna(subset=['alcohol'], inplace