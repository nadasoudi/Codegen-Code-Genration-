import pandas as pd

df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})

df.columns = ["A", "B", "C"]
df.index = ["Row 1", "Row 2", "Row 3"]

print(df)

# Solution:

df.columns = ["A", "B", "C"]
df.index =