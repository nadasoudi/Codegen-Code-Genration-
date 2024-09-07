# Create a Pandas dataframe
df = pd.DataFrame({'Male': [1, 2, 3, 4, 5],
                   'Female': [2, 4, 6, 8, 10],
                   'Child': [3, 5, 7, 9, 11]})

# Create a Pivot table
pivot = df.pivot_table(index='Male', columns='Child', values='Female')

# Print the result
print(p