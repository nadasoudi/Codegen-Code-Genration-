import pandas as pd

# Create a dataframe
df = pd.DataFrame({'Name': ['Rolf', 'Charlie', 'Anna', 'Bob', 'Jen', 'Sue'],
                   'Score': [85, 90, 95, 100, 95, 90]})

# Create a subset of the dataframe
df_subset = df.loc[df['Score'] >= 60]

# Print the subset of the dataframe
print(df_sub