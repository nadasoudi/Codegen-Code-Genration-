import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv('Alphabet Inc.csv')

# Create a new dataframe with the columns 'Date' and 'Open'
df_new = df[['Date', 'Open']]

# Create a new dataframe with the columns 'Date' and 'Open'
df_new = df_new.rename(column