import pandas as pd
import datetime

# Read the data from the csv file
df = pd.read_csv('/Users/srinivasan/Downloads/data.csv')

# Create a new column called 'date'
df['date'] = pd.to_datetime(df['date'])

# Create a new column called 'time'
df['time'] = df['date'].dt.time

# Create a new