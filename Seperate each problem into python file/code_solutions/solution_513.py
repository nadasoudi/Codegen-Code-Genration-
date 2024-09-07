import pandas as pd

df = pd.read_csv('world_alcohol_consumption.csv')

df['WHO region, Country, Beverage Types'] = df['WHO region, Country, Beverage Types'].str.replace('Americas', 'Americas')
df['WHO region, Country, Beverage Types'] =