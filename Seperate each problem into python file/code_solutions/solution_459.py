import pandas as pd
import numpy as np

# Create a dataframe from the csv file
df = pd.read_csv('data.csv')

# Create a new column named 'year'
df['year'] = df['date'].dt.year

# Create a new column named'month'
df['month'] = df['date'].dt.month

# Create a new column named 'day'
df['day']