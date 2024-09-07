import pandas as pd

# Read the data from the csv file
df = pd.read_csv('UFO_data.csv')

# Create a new column called 'Reporting_date'
df['Reporting_date'] = pd.to_datetime(df['Reporting_date'])

# Create a new column called 'Unidentified_UFO'
df['Unidentified_UFO'] = df['Unidentified_UFO'].str.replace