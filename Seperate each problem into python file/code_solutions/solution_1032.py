import pandas as pd

df1 = pd.read_excel('coalpublic2013.xlsx')
df2 = pd.read_excel('coalpublic2013.xlsx')
df3 = pd.read_excel('coalpublic2013.xlsx')

df = pd.concat([df1, df2, df3], axis=0)

df