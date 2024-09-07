import pandas as pd
import datetime

df = pd.read_csv('https://github.com/datasets/csv/blob/master/data/airline.csv?raw=true')

df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].dt.strftime('%m-%d-%Y')

print(df