import pandas as pd
import numpy as np

# Read the data
df = pd.read_csv('../data/data.csv')

# Create a groupby object
groupby = df.groupby(['gender', 'age'])

# Group the data by gender and age
grouped = groupby.aggregate(['mean','sum'])

# Sort the grouped data
grouped.sort_values(by