import pandas as pd

# Read the data
df = pd.read_csv("data/height-weight.csv")

# Create a groupby object
groupby_object = df.groupby(['Height', 'Weight'])

# Count the rows
print(groupby_object.size())

# Create a dictionary to store the result
result = {}

# Iterate over the groupby object
for name, group in groupby_object: