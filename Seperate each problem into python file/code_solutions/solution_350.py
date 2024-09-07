import pandas as pd

df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [10, 20, 30, 40, 50]})

df.index = ["a", "b", "c", "d", "e"]

print(df)

# Solution:

# df.drop("A", axis=1)

# Solution:

# df.drop(["a",