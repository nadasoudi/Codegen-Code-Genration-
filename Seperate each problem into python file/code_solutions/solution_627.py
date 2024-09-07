import pandas as pd

df1 = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [10, 20, 30, 40, 50]})
df2 = pd.DataFrame({"A": [10, 20, 30, 40, 50], "B": [100, 200, 300, 400, 500]})

df = pd.merge(df1, df2, on="A")

print(df)