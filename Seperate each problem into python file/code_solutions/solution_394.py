import pandas as pd

# Read the data from the excel file
df = pd.read_excel('employee.xlsx')

# Create a Pandas dataframe from the data
df2 = pd.DataFrame(df)

# Print the head of the dataframe
print(df2.head())

# Print the shape of the dataframe
print(df2.shape)

#