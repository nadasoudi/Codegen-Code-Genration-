import pandas as pd

df = pd.read_csv("C:\\Users\\DELL\\Desktop\\Python\\Data_Visualization\\cabin_class.csv")

df.head()

df.columns

df.shape

df.dtypes

df.describe()

df.isnull().sum()

df.dropna(inplace=True)

df.head()

df.