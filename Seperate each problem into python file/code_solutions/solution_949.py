import pandas as pd
import numpy as np

df1 = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [10, 20, 30, 40, 50]})
df2 = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col3': [10, 20, 30, 40, 50]})

df = pd.concat([df1