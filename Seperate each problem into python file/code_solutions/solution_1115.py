import pandas as pd

# Read the data
data = pd.read_csv('time_series.csv')

# Create a new column in the dataframe
data['timezone'] = data['date'].dt.tz_localize(None)

# Remove the timezone information
data = data.drop(columns=['date', 'timezone'])

# Write the dataframe to a new csv file
data.to_csv('time_zone_