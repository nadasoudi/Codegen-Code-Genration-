import pandas as pd

# Create a Pandas Dataframe
df = pd.DataFrame({'col1': [1, 2, 3, 4, 5],
                   'col2': [10, 20, 30, 40, 50]})

# Insert row at given position in Pandas Dataframe in Python
df.loc[0, 'col1'] = 100

# Print the new Dataframe
print(df)

# Create a Pandas Dataframe
df = pd.DataFrame({