import pandas as pd

left = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
right = pd.DataFrame({'c': [7, 8, 9], 'd': [10, 11, 12]})

left.join(right, on='a')

# OUTPUT:
# a   b   c   d
# 1   1   4   7