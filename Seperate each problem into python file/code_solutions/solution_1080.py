import pandas as pd
import numpy as np

df = pd.read_csv('https://github.com/jbrownlee/Datasets/blob/master/iris.csv')

# Create a pivot table
pivot = df.pivot_table(index='class', columns='gender', values='solo_boarding', aggfunc='count')

# Print the pivot table
print(pivot)