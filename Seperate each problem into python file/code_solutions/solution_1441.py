import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Alphabet Inc_data.csv')

df['Date'] = pd.to_datetime(df['Date'])

df.set_index('Date', inplace=True)

plt.scatter(df['Volume'], df['Price'])

plt.show()

"""