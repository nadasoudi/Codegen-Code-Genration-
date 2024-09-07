import pandas as pd

df = pd.read_csv('https://github.com/jbrownlee/Datasets/blob/master/UFO%20Visits.csv?raw=true')

df['Year'] = df['Year'].astype(str)
df['Year'] = df['Year'].str.replace('[^0-9]', '')
df['Year'] = df