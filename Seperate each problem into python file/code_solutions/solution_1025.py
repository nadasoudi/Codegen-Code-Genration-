import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv('alphabet_inc_data.csv')

# Create a new dataframe with only the columns we want
df = df[['Date', 'Adj Close']]

# Create a new dataframe with only the columns we want
df = df[