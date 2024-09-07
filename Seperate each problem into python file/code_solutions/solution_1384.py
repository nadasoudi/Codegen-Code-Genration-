import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv('Alphabet Inc_Stock_Price_Data.csv')

# Create a new dataframe with only the columns we want
df_new = df[['Date', 'Open', 'High', 'Low', 'Close']]

# Create a new dataframe with only the columns we want
df_new