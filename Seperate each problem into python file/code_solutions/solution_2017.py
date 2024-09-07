import pandas as pd

# Read the Excel file
df = pd.read_excel('C:\\Users\\srin\\OneDrive\\Desktop\\Python\\Excel_File.xlsx', sheet_name='Sheet1')

# Extract the date from the Excel file
df['Date'] = pd.to_datetime(df['Date'])

# Print the date
print(df['Date'])

# Print the date in a specific format
print(df['Date'