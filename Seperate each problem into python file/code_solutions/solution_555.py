import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Alphabet Inc.csv')

df['Date'] = pd.to_datetime(df['Date'])

df.set_index('Date', inplace=True)

plt.barh(df.index, df['Open'], color='#00ff00')

plt.show()