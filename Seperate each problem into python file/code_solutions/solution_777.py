import pandas as pd

df = pd.read_excel('coalpublic2013.xlsx')

df.head()

df.tail()

df.shape

df.columns

df.columns = ['Year', 'Coal', 'Coal_Total', 'Coal_Total_Total', 'Coal_Total_Total_Total', 'Coal_Total_Total_Total_