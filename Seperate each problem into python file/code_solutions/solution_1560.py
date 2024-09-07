import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Alphabet Inc_stock_price_data.csv')

df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

plt.hist(df['Close'], bins=30)