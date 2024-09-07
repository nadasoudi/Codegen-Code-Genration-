import pandas as pd

df = pd.read_csv("../data/class_survival.csv")

df.groupby(['gender', 'class']).survived.sum().unstack().plot(kind='bar')

# %%