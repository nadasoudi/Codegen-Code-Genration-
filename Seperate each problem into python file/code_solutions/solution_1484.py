import pandas as pd

# Create a dataframe
df = pd.DataFrame({'Name': ['Rolf', 'Charlie', 'Anna', 'Bob'],
                   'Age': [30, 32, 33, 34],
                   'Score': [85, 90, 95, 100]})

# Create a new column
df['Age'] = df['Age'].apply(lambda x: x * 2)

# Print the dataframe
print(df)