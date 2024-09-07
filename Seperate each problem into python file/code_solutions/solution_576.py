import pandas as pd

df = pd.read_csv('/Users/srinivasan/Downloads/airline_passengers.csv')

df.groupby(['Month','UFO']).size().unstack().plot(kind='bar')

# %%