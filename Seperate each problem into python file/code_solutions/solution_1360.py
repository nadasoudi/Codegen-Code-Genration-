import pandas as pd

# Read the data from Salesdata.xlsx
df = pd.read_excel('Salesdata.xlsx')

# Create a Pivot table with multiple columns
pivot = df.pivot_table(index='Customer', columns='Month', values='Sales')

# Print the result
print(pivot)

# Create a Pivot table with multiple rows
pivot = df.