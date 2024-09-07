import pandas as pd

df = pd.DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    columns=['a', 'b', 'c'],
    index=['one', 'two', 'three']
)

print(df)

# Solution:

# df = pd.DataFrame(
#     [[1, 2, 3], [4, 5, 6], [7, 8, 9