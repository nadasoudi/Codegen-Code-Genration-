import pandas as pd

df = pd.read_csv("C:\\Users\\DELL\\Desktop\\Python\\Data_Visualization\\Sales.csv")

# Create a pivot table
pivot = df.pivot_table(index="Customer ID", columns="Item", values="Sales")

# Find the maximum and minimum sales
print(pivot.max())
print(pivot.min())

# Create a new column in the pivot