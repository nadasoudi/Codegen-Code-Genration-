df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                   'B': [10, 20, 30, 40, 50]})

# Iterate over rows in the Dataframe
for row in df.iterrows():
    print(row)

# Iterate over columns in the Dataframe
for col in df.columns:
    print(col)

# Iterate over rows and columns in the Dataframe
for row, col in df.iterrows