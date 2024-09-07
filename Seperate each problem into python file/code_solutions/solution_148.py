import pandas as pd
import numpy as np

df = pd.read_csv('/Users/srinivasan/Desktop/Python/data/data.csv')

df['sentence'] = df['text'].apply(lambda x: x.split('.'))

df['sentence'] = df['sentence'].apply(lambda x:''.join(x))

df['sentence'] = df['sentence'].apply(lambda