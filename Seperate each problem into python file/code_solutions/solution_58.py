import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/glassdoor.csv')
df.head()

df.isnull().sum()

df.dropna(inplace=True)
df.isnull().sum()

df.head()

df.isnull().sum()

df.dropna(inplace=True)
df.isnull().sum