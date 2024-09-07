import pandas as pd
import numpy as np

# Create a Pandas dataframe
df = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])

# Create a Pivot table
pivot = df.pivot_table(index='a', columns='b', values='c', aggfunc='sum')

# Compute the survival totals
print(pivot.loc[