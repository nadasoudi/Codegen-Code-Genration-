import pandas as pd

# Read the data
df = pd.read_csv('/Users/srinivasan/Downloads/UFO_Sighting_Report.csv')

# Calculate the average
df['UFO_Sighting_Report_Average'] = df['UFO_Sighting_Report'].mean()

# Print the average
print(df['UFO_Sighting_Report_Average'])

# Create a