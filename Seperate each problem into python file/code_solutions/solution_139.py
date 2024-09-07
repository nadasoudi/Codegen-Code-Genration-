import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the csv file
df = pd.read_csv('/Users/krishna/Downloads/UFO_sighting_data.csv')

# Create a new dataframe with only the columns that are required
df_new = df[['month', 'UFO_id', 'UFO_name', 'UFO_type', 'UFO