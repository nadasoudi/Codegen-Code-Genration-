import pandas as pd

df = pd.DataFrame({"col1": [1, 2, 3, 4, 5], "col2": [1, 2, 3, 4, 5], "col3": [1, 2, 3, 4, 5]})

print(df.empty)

# Output:
# True
# True
# True
# False

# Create a new DataFrame: df_empty
df_empty = pd