import pandas as pd

# Read the data from the excel file
data = pd.read_excel('data.xlsx')

# Create a new column in the dataframe
data['new_column'] = data['new_column'].fillna(value=data['new_column'].mean())

# Print the dataframe
print(data)

# Create a new column in the dataframe
data['new_