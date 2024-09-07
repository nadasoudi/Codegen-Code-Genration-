import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv('Alphabet Inc.csv')

# Create a stacked bar plot
df.groupby(['Date'])['Open'].sum().plot(kind='bar', figsize=(10, 7))

# Create a stacked bar plot
df.groupby(['Date'