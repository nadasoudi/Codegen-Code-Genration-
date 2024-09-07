import pandas as pd

# Read the data
df = pd.read_csv('vowels.csv')

# Create a new column named 'vowels_with_two_vowels'
df['vowels_with_two_vowels'] = df['vowels'].str.contains('[aeiou]')

# Print the dataframe
print(df)

# Create a new column named 'vow