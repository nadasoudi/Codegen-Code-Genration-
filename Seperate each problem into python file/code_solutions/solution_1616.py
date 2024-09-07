import pandas as pd

# Create a dataframe from the given data
df = pd.DataFrame({"A": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "B": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})

# Create a new column in the dataframe called "Frequency"
df["Frequency"] = df["A"].apply(lambda x: