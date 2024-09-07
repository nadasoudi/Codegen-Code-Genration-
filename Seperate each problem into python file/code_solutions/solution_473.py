import pandas as pd

# Create a time series object
ts = pd.Series(range(1, 101), index=pd.date_range('1/1/2000', periods=100))

# Create a time series object with a time zone
ts_tz = ts.tz_localize('Asia/Kolkata')

# Create a time series object with a time zone
ts_tz_2 = ts.tz_localize('Asia/Kolkata', ambiguous='Na