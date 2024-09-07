import pandas as pd

# Create a dataframe
df = pd.DataFrame(
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
    index=['a', 'b', 'c', 'd'],
    columns=['one', 'two', 'three', 'four']
)

# Create a new dataframe with only the rows that