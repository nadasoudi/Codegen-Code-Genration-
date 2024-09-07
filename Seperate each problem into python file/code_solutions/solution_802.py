import pandas as pd

# Read the data from the file
df = pd.read_csv("data.csv")

# Extract the number from the column "Number"
print(df["Number"].head(1))

# Extract the number from the column "Number"
print(df["Number"].head(1).values)

# Extract the number from the column "Number"
print(df["Number"].head(1).values[0])