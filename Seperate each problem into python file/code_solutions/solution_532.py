import pandas as pd

df = pd.read_csv('https://github.com/jbrownlee/Datasets/blob/master/pandas_datareader/data/election_data.csv?raw=true')

df['Election_results'] = df['Election_results'].str.upper()

df.head()

df.head()

df.head()

df.head()

df