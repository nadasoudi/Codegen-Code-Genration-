import pandas as pd
import datetime

df = pd.read_csv('https://github.com/datasets/ufo-data/raw/master/data/ufo-data.csv')
df['date'] = pd.to_datetime(df['date'])
df['date'] = df['date'].dt.date
df['date'] = df['date'].dt.strftime('%