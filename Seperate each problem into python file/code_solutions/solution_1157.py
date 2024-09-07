import pandas as pd

df = pd.read_csv('world_alcohol_consumption.csv')

df = df[df['Year'] >= '1960']

df = df[df['Year'] <= '1980']

df = df[df['World'] >= '0-1']

df = df[df['World'] <= '10']

df = df[df['World'] >= '10-20']