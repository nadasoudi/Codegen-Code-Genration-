import pandas as pd

df = pd.read_csv('https://github.com/jbrownlee/Datasets/blob/master/Alcohol-Consumption/Alcohol-Consumption.csv')

df.head()

df.shape

df.sample(frac=0.1)

df.sample(frac=0.1, random_state=42)

df.sample(frac=0.1, random_