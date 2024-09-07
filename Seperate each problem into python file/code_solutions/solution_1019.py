import pandas as pd
import datetime

# Read the data from the file
df = pd.read_csv('unidentified_object.csv')

# Extract the year, month, day, hour, minute, second and weekday from the dataframe
df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month
df['day'] = df['Date'