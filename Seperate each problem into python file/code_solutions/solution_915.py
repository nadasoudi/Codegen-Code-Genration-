import pandas as pd

# Create a DataFrame
df = pd.DataFrame(
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
    index=pd.MultiIndex.from_product([['a', 'b', 'c'], ['d', 'e', 'f']]),
    columns=pd.MultiIndex.from_product([['a', 'b', '