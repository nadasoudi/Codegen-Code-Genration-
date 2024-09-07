import pandas as pd

# Read the data
df = pd.read_csv('world_beverages.csv')

# Create a new column 'Beer'
df['Beer'] = df['World_Beverages'].apply(lambda x: 'Beer' if x >= 5 else 'Not Beer')

# Create a new column 'Beer_Types'
df['Beer_Types'] = df['Beer'