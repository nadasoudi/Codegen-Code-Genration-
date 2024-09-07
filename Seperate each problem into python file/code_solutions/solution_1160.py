import pandas as pd

df = pd.read_csv("https://github.com/datasets/csv/raw/master/data/finance.csv")

df.groupby(['first_name', 'last_name']).agg(
    {'balance': ['sum']}).reset_index()

df.groupby(['first_name', 'last_name']).agg(
    {'balance': ['