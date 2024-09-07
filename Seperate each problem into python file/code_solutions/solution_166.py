import pandas as pd

df = pd.read_csv("C:\\Users\\DELL\\Desktop\\Python\\Sales_Sales.csv")

df.groupby(['Sales','Manager']).size().unstack().plot(kind='bar',stacked=True)

# Create a pivot table to display the sales of each manager and the mean sale amount of each manager.

df.groupby(['Sales','Manager']).size().un