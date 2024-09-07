import pandas as pd

df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [10, 20, 30, 40, 50]})

# Convert the dataframe to NumPy array
arr = df.to_numpy()

# Convert the NumPy array to Pandas dataframe
df = pd.DataFrame(arr, columns=["A", "B"])

# Print the dataframe
print(