import pandas as pd

# Create a dictionary
d = {'a': 1, 'b': 2, 'c': 3}

# Create a dataframe
df = pd.DataFrame(d)

# Print the dataframe
print(df)

# Create a dataframe from a list of dictionaries
df2 = pd.DataFrame(d, columns=['a', 'b', 'c'])

# Print the dataframe
print(df2)