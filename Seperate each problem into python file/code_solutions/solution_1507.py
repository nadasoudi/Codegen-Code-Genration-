import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv('Alphabet Inc.csv')

# Create a histogram plot
plt.hist(df['Open'], bins=30)

# Format the plot
plt.title('Histogram of Alphabet Inc. Opening Price')
plt.xlabel('Opening Price')
plt.