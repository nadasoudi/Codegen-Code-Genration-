import pandas as pd
import datetime

# Read the data from the csv file
df = pd.read_csv('/Users/srinivasan/Desktop/Python/data/data.csv')

# Extract the day name from the date
date = df['Date']
day_name = date.dt.strftime('%A')

# Add 2 days and 1 business day with the specified date
date = date.