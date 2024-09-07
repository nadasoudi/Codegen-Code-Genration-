import pandas as pd

df = pd.read_csv('dataset.csv')

df = df[df['average_consumption'] > 2.50]

df.to_csv('dataset_filtered.csv', index=False)

# Solution:

# df = pd.read_csv('dataset_filtered.csv')
# df = df[df['average