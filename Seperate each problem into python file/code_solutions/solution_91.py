import pandas as pd

df = pd.read_csv('world_alcohol_consumption.csv')

df.head()

df.columns

df.columns = ['Year', 'World_alcohol_consumption']

df.head()

df.columns

df.columns = ['Year', 'World_alcohol_consumption', 'Alcohol_consumption']

df.head