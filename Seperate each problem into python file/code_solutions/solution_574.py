import pandas as pd

# Create a dataframe from the given data
df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [1, 2, 3, 4, 5], "C": [1, 2, 3, 4, 5]})

# Sort the dataframe by the column "A"
df.sort_values(by="A", ascending=True)

# Sort the dataframe by the column "B"
df.sort_values