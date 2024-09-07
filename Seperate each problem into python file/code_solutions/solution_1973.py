import pandas as pd

df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [10, 20, 30, 40, 50]})

df.drop("B", axis=1)

df.drop("A", axis=0)

df.drop("B", axis=1, inplace=True)

df.drop("A", axis=0, inplace=True)

df.drop("B", axis=1