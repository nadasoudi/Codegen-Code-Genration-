import pandas as pd

# Read the data
df = pd.read_csv("data/pima-indians-diabetes.csv")

# Create a new column called 'Status'
df['Status'] = df['Outcome'].map({'Not Available': 0, 'Available': 1})

# Remove the 'Outcome' column
df = df.drop('Outcome', axis=1)