import pandas as pd

df = pd.read_csv('https://github.com/jbrownlee/Datasets/blob/master/UFO%20Visits.csv?raw=true')

df['Year'] = df['Year'].astype(str)
df['Month'] = df['Month'].astype(str)

df['UFO'] = df['UFO'].astype(str)