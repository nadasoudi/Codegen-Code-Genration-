import pandas as pd

# Read the data
df = pd.read_csv("data/data.csv")

# Create a new column called "Most Frequent"
df["Most Frequent"] = df["Age"].mode()

# Print the dataframe
print(df)

# Replace the missing values with the most frequent values
df.fillna(df.mode(), inplace=True)

# Print the dataframe