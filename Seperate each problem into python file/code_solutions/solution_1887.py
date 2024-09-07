import pandas as pd

# Create a dataframe
df = pd.DataFrame({'Name': ['Rolf', 'Charlie', 'Anna', 'Bob', 'Jen', 'Sue'],
                   'Score': [85, 90, 95, 100, 95, 90]})

# Create a column based on the condition
df['Score'] = df['Score'].apply(lambda x: x if x >= 90 else x - 10)

# Display the dataframe
print(