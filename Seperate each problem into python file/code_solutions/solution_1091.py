import pandas as pd

# Read the data
df = pd.read_csv('purchase_data.csv')

# Group by customer id
grouped = df.groupby('customer_id')

# Get mean, min, and max values
mean = grouped.mean()