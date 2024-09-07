import pandas as pd
import numpy as np

df = pd.read_csv("https://github.com/jbrownlee/Datasets/blob/master/pivot_table.csv?raw=true")

df.head()

df.columns = ['Region', 'Item', 'Unit Sold']

df.head()

df.head(5)

df.head(5).Region

df.head(