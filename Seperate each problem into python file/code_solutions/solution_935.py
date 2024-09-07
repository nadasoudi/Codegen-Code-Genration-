import pandas as pd

# Read the data from the excel file
df = pd.read_excel('data.xlsx')

# Add the summation to the row
df['summation'] = df['summation'].apply(lambda x: x + df['summation'])

# Write the dataframe to the excel file
df.to_excel('summation.xlsx')

# Read the data from the excel file