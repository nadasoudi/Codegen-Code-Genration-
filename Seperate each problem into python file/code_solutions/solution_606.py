import pandas as pd

# Create a dataframe
df = pd.DataFrame({'Item': ['Apples', 'Oranges', 'Bananas', 'Carrots', 'Cherries', 'Pears'],
                   'Quantity': [4, 2, 4, 1, 2, 5]})

# Create a new column
df['Is_Not_Common'] = df['Item'].apply(lambda x: x not in df['Item'])

# Print