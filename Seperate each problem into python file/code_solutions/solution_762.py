import pandas as pd

df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [10, 20, 30, 40, 50]})
print(df)

df.replace({"A": 10, "B": 20}, inplace=True)
print(df)

df.replace({"A": 10, "B": 20}, inplace=True, regex=True)
print(df)