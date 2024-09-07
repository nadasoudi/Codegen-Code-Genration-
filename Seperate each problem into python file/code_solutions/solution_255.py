import pandas as pd
import numpy as np

titanic = pd.read_csv('titanic.csv')

# Create a pivot table with multiple columns
pivot = titanic.pivot_table(index='Sex', columns='Pclass', values='Survived')

# Print the pivot table
print(pivot)

# Create a pivot table with multiple rows
pivot = titanic.pivot_table(index