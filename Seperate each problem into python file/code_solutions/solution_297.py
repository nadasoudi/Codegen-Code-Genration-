import pandas as pd

df = pd.read_csv('tweets.csv')

df['mention'] = df['text'].apply(lambda x: "@" in x)

print(df.head())

df.to_csv('tweets_with_mentions.csv')

# Solution:

# df = pd.read_csv('tweets.csv')
# df['mention']