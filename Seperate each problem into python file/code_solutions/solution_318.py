import pandas as pd

series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

df = pd.DataFrame(series)

df.index.name = 'index'

print(df)

# Solution:

# import pandas as pd

# series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8