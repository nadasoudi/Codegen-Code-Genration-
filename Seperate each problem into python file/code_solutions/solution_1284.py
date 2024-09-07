import pandas as pd
import hashlib

df = pd.read_csv('hash_word.csv')

# Hash the word
hash_word = hashlib.sha256(df['text'].values.tolist()).hexdigest()

# Hash the word
hash_word = hashlib.sha256(df['text'].values.tolist()).hexdigest()

# Hash the word
hash_word =