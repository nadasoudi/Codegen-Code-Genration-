import pandas as pd

df = pd.read_csv('https://github.com/jbrownlee/Datasets/blob/master/ufo.csv?raw=true')

df['hour'] = df['hour'].astype(int)

df['year'] = df['year'].astype(int)

df['year'] = df['year'].astype(str)

df