pivot_table(df, columns=['Item_Name'], values='Sale_Price')

"""

# Solution 1

import pandas as pd
import numpy as np

df = pd.read_csv('https://github.com/jbrownlee/Datasets/blob/master/pivot_table.csv?raw=true')

# Create a pivot table
df.pivot_table(values='Sale_Price