pivot_table(df, columns=['Item_Name', 'Sale'], values='Sale', aggfunc='max')

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('pivot_table.csv')

# Create a Pandas dataframe from the dataframe
df = pd.DataFrame(df)

# Create a Pandas