import pandas as pd

df = pd.read_csv('../data/pandas_data.csv')

df['punctuation'] = df['text'].str.extractall(r'[^\w\s]')

print(df['punctuation'])

# Solution:

# df['punctuation'] = df['text'].str.extractall(r'[^\w\s]')
#