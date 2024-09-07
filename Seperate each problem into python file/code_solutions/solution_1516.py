import pandas as pd

# Read the data
df = pd.read_csv('../data/data.csv')

# Create a new dataframe with the autocorrelation of the numeric columns
autocorr = df.corr()

# Print the first 5 rows of the dataframe
autocorr.head()

# Create a new dataframe with the autocorrelation of the numeric columns
autocorr = df.corr()

# Print the