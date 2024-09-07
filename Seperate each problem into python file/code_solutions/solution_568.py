import pandas as pd

# Read the data
df = pd.read_csv('world_alcohol_consumption.csv')

# Create a new column'region'
df['region'] = df['region'].replace('Americas', 'Americas')
df['region'] = df['region'].replace('Europe', 'Europe')

# Create a new column