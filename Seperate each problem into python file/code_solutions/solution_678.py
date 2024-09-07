import pandas as pd

# Read the data
df = pd.read_csv('/Users/krishna/Downloads/UFO_Data.csv')

# Create a new dataframe with only unique reporting dates
df_unique = df.drop_duplicates(subset=['Reporting_Date'])

# Print the dataframe
print(df_unique)

# Create a new dataframe with only unique reporting dates
df_unique = df.drop