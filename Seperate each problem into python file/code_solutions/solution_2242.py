import pandas as pd

# Read the data
df = pd.read_csv('https://github.com/datasets/titanic/raw/master/train.csv')

# Create a new column with the first name
df['first_name'] = df['first_name'].str.lower()

# Create a new column with the last name
df['last_name'] = df['last_name'].str.lower()

# Create a new column with the title
df['