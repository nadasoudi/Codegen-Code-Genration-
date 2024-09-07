import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [5, 6, 7, 8]})

# Insert a column at the index 0
df.insert(0, 'col3', [10, 20, 30, 40])

# Print the DataFrame
print(df)

# Create a DataFrame
df = pd.DataFrame({'