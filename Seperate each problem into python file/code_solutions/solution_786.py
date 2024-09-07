import pandas as pd

df = pd.read_csv("C:\\Users\\DELL\\Desktop\\Python\\Data_Visualization\\cabin_class.csv")

df.head()

df.columns

df.columns = ['Cabin Class', 'Count']

df.head()

df.head(5)

df.head(5).Count

df.head(5).Cabin Class