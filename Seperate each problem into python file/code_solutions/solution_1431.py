import pandas as pd

# Create a time series
hour = pd.Series(pd.date_range('1/1/2000', periods=24, freq='H'))
minute = pd.Series(pd.date_range('1/1/2000', periods=24, freq='T'))

# Create a time series
hour = pd.Series(pd.date_range('1/1/2000', periods=24, freq='H'))
minute