import pandas as pd

# Create a Timedelta Index
tdi = pd.date_range('1/1/2000', periods=4, freq='D')

# Create a Period Index
pi = pd.period_range('2000-01-01', periods=4, freq='D')

# Create a DateTime Index
dt = pd.date_range('2000-01-01', periods=4, freq='D')

# Create a