import pandas as pd
import numpy as np

# Read the data from the csv file
df = pd.read_csv('data.csv')

# Create a new dataframe with the columns 'x' and 'y'
df_new = df.copy()

# Create a new dataframe with the columns 'x' and 'y'
df_new['x'] = df['x']
df_new['y'] = df['y']

# Create