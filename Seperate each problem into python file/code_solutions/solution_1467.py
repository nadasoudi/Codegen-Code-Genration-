import pandas as pd
import numpy as np

df = pd.read_csv('https://github.com/jbrownlee/Datasets/blob/master/pima-indians-diabetes.csv')

# Create a pivot table
pivot = df.pivot_table(index='Outcome', columns='Sex', values='Age', aggfunc='sum')

# Create a separate table for