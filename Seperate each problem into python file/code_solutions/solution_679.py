import pandas as pd
import numpy as np

df = pd.read_csv('https://github.com/jbrownlee/Datasets/blob/master/iris.csv')

# Create a pivot table
pivot = df.pivot_table(index='species', columns='class', values='petal_length', aggfunc='mean')

# Find survival rate by gender
pivot['survived'] =