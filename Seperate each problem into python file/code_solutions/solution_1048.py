import pandas as pd

df = pd.read_csv("https://github.com/datasets/csv/blob/master/data/airline.csv?raw=true")

df.head()

df.pivot_table(values='airline_fare', index='day', columns='month', aggfunc='sum')

df.head()

df.pivot_table(values='airline_fare', index='day', columns='