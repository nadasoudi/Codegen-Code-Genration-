import pandas as pd

df = pd.read_csv("world_alcohol_consumption.csv")

df = df[df["Alcohol"]!= 0]

df.head()

df.shape

df.columns

df.columns = ['Alcohol', 'Consumption']

df.head()

df.head(5)

df.head(5).Alcohol