import pandas as pd

df = pd.DataFrame({'Name': ['Rolf', 'Charlie', 'Anna', 'Bob', 'Jen', 'Sue'],
                   'Score': [87, 95, 100, 100, 100, 100]})

print(df['Name'].str.contains('Rolf'))

# Solution:

import pandas as pd

df = pd.DataFrame({'Name': ['R