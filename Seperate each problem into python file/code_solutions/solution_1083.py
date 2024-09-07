import pandas as pd

df = pd.read_csv('world-alcohol-consumption.csv')

df['Beer'] = df['Beer'].apply(lambda x: 1 if x >= 4 else 0)
df['Wine'] = df['Wine'].apply(lambda x: 1 if x >= 4 else 0)
df['Spices'] = df['Spices'].apply(