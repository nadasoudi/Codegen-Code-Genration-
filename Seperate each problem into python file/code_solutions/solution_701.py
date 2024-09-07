import pandas as pd
import numpy as np

df = pd.read_csv('world_alcohol_consumption.csv')

df['region'] = df['region'].str.lower()
df['country'] = df['country'].str.lower()

df['region'] = df['region'].replace('western pacific', 'western pacific