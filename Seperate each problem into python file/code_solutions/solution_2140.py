import pandas as pd

series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Create a dataframe from the series
df = pd.DataFrame(series)

# Print the head of the dataframe
print(df.head())

# Print the tail of the dataframe
print(df.tail())

# Print the shape of the dataframe
print(df.shape)

# Print the head and tail of the data