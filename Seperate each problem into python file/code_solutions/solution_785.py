import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Alphabet Inc.csv')

df['Date'] = pd.to_datetime(df['Date'])

df.set_index('Date', inplace=True)

plt.bar(df.index, df['Open'])

plt.show()

"""

import pandas as p