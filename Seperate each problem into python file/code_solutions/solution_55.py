import pandas as pd

# Read the data from the file
df = pd.read_csv('data.csv')

# Extract only the words from the column
words = df['text'].str.split(' ')

# Extract only the words from the column
words = words.str.get_dummies(sep=' ')

# Print the words extracted
print(words)

# Create a new column in the DataFrame called 'words'