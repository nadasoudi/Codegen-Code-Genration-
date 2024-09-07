import pandas as pd
import numpy as np

# Create a time series object
ts = pd.Series(np.random.randn(100), index=pd.date_range('1/1/2000', periods=100))

# Select the dates between certain dates
ts_dates = ts.index.between('2000-01-01', '2000-01-10')

# Select the dates between