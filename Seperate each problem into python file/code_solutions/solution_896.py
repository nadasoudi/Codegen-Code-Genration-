df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
df2 = pd.DataFrame({'a': [7, 8, 9], 'b': [10, 11, 12]})

df1.join(df2, on='a')

"""

import pandas as pd
import numpy as np

df1 = pd.DataFrame({'a': [1,