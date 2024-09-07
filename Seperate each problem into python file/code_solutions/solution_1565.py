import pandas as pd

series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(series.diff())

series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(series.diff(periods=2))

series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9