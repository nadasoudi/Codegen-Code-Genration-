import pandas as pd

# Create a time-series with two index labels and random values
ts = pd.Series(np.random.randn(100), index=['Jan', 'Feb'])

# Print the type of the index
print(type(ts.index))

# Create a time-series with two index labels and random values
ts = pd.Series(np.random.randn(100), index=['