import pandas as pd
import numpy as np

df = pd.DataFrame({'col1': [1, 2, 3, 4, 5], 'col2': [10, 20, 30, 40, 50]})

s = pd.Series([1, 2, 3, 4, 5])

print(df.eq(s))

# Output:
#     True
#     True
#     True
#     False
#