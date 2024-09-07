import pandas as pd

# Read the data into a dataframe
df = pd.read_excel('employee.xlsx', sheet_name='Sheet1')

# Sort the dataframe based on multiple columns
df = df.sort_values(['Name', 'Age', 'Job'])

# Print the dataframe
print(df)

# Create a Pandas Excel writer using X