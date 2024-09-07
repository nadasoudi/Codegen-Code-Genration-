import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [10, 20, 30, 40, 50]})

# Create a Series
s = pd.Series([1, 2, 3, 4, 5])

# Create a DataFrame from a Series
df2 = pd.DataFrame(s)

# Create a Series from a DataFrame
s2 = pd