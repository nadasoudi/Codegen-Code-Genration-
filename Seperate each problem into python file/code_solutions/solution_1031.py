import pandas as pd

df = pd.read_csv('datasets/WHO_region.csv')
df.drop_duplicates(subset=['WHO region'], inplace=True)
df.to_csv('datasets/WHO_region_duplicates.csv')

"""

# Solution

import pandas as pd

df = pd.read_csv('datasets/WHO_region.csv