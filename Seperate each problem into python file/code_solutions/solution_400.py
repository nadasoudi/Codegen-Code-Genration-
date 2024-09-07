import pandas as pd

df = pd.DataFrame(
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
    index=['a', 'b', 'c', 'd'],
    columns=['x', 'y', 'z', 'w']
)

print(df)

# Solution:

# df = pd.DataFrame(
#