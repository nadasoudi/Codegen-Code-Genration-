import pandas as pd

# Create a dataframe from the string data
data = pd.Series(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Create a timeseries from the dataframe
ts = pd.Series(data)

# Create a timeseries from the string data
ts = pd.Series(data.str.split('-'))