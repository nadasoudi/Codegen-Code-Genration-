import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv('/Users/krishna/Downloads/UFO_observation_time.csv')

# Create a plot
plt.figure(figsize=(10, 6))
plt.hist(df['observation_time'], bins=50)
plt.show()

# Create a plot