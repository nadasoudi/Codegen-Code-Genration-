import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Alphabet Inc.csv')

df['Date'] = pd.to_datetime(df['Date'])

df.set_index('Date', inplace=True)

df.plot(kind='line', figsize=(10, 6))

plt.show()

"""

import pandas