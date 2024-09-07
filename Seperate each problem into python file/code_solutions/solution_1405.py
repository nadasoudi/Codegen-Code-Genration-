import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv('/Users/srinivasan/Downloads/UFO_Sightings.csv')

# Create a new dataframe with only the columns that are required
df_new = df[['Year', 'Sightings']]

# Create a new dataframe with only the columns that are required
df_new = df