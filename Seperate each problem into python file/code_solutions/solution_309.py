import pandas as pd

series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

result = series.is_monotonic_increasing
print(result)

result = series.is_monotonic_decreasing
print(result)

result = series.is_unique
print(result)

result = series.is_monotonic
print(result)