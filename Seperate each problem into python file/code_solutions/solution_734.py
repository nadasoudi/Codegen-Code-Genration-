import pandas as pd
import datetime as dt

start = dt.datetime(2020, 1, 1)
end = dt.datetime(2020, 1, 10)

periods = 10

df = pd.DataFrame({"start": [start], "end": [end]})

print(df)

# Solution:

# df = pd.DataFrame({"start": [start], "end": [end