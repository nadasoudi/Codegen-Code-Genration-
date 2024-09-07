import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/world_alcohol_consumption.csv')
df.rename(columns={'gdpPercap': 'gdp_per_cap'}, inplace=True)
df.rename(columns={'lifeExp': 'life_exp'}, inplace=True)
df.rename(column