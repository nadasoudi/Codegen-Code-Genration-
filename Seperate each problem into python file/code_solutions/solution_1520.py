import pandas as pd

# Read the data into a pandas dataframe
df = pd.read_excel('employee.xlsx')

# Sort the dataframe by the hire_date column
df.sort_values(by='hire_date', inplace=True)

# Print the dataframe
print(df)

# Create a Pandas dataframe from the dataframe