import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Alphabet Inc.csv')

df['Date'] = pd.to_datetime(df['Date'])

df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

df['Volume'] = df['Volume'].astype(float)

df['Trading