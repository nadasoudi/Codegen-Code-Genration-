import pandas as pd

# Read the data into a DataFrame
df = pd.read_csv('/Users/srinivasan/Desktop/Python/data/data.csv')

# Create a list of words
words = df['text'].str.split(' ', expand=True)

# Extract the first word of each row
words = words.iloc[:, 0]

# Print the first word of each row
print(words)