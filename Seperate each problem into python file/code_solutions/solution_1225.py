import pandas as pd

# Read the data
df = pd.read_csv('/Users/krishna/Downloads/UFO_Data.csv')

# Create a new dataframe with only the columns that are not 'Unidentified'
df_new = df[df['Unidentified'] == False]

# Create a new dataframe with only the columns that are not 'Unidentified'
df_new = df[df