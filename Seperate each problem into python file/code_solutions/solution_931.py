import pandas as pd

df = pd.read_csv('https://github.com/jbrownlee/Datasets/blob/master/Alcohol-Consumption/world_alcohol.csv')
df.head()

df.columns

df.columns = ['Year', 'Country', 'Alcohol', 'Consumption']

df.head()

df.head(2)

df.head(2, columns=