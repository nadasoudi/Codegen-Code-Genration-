import pandas as pd

df = pd.read_csv("https://github.com/datasets/csv/raw/master/data/finance.csv")

df.head()

df.groupby(['year', 'quarter']).size().unstack().plot(kind='bar', stacked=True)

df.groupby(['year', 'quarter']).size().unstack().plot(kind='bar', stacked