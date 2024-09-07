import pandas as pd

df = pd.read_csv("C:\\Users\\DELL\\Desktop\\Python\\Sales.csv")

df.head()

df.columns = ['Region', 'Sales']

df.head()

df.Sales.plot(kind='bar')

df.Sales.plot(kind='barh')

df.Sales.plot(kind='barh')

df.Sales.plot(kind='barh