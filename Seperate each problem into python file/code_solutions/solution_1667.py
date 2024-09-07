import pandas as pd

# Read the data
df = pd.read_csv("data/data.csv")

# Replace NaNs with median or mean of the specified columns
df.fillna(df.median(), inplace=True)

# Print the dataframe
print(df)

# Create a new dataframe with the median or mean of the specified columns
df_median = df.copy()
df_median.fill