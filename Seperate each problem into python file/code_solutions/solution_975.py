df1 = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
df2 = pd.DataFrame({'col1': [7, 8, 9], 'col2': [10, 11, 12]})

df1.merge(df2, on='col1')

"""

import pandas as pd
import numpy as np

df1 = pd.DataFrame({'col1