import pandas as pd
import datetime as dt

# Create a dataframe
df = pd.DataFrame(columns=['Date', 'Daily Frequency'])

# Create a loop to iterate over the dates
for i in range(1, 32):
    # Create a new date
    new_date = dt.date(2021, i, 1)
    # Create a new frequency
    new_frequency =