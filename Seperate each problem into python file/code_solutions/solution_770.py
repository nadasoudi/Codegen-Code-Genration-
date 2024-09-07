import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/glassdoor.csv')
df.head()

df.columns

df.index

df.iloc[:,0:3]

df.iloc[:,0:3].columns

df.iloc[:,0:3].columns