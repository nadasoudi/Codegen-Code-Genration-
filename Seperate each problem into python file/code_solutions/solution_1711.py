import pandas as pd

df = pd.DataFrame({"A": [1, 2, 3, 4, 5],
                  "B": [10, 20, 30, 40, 50],
                  "C": [100, 200, 300, 400, 500]})

df.stack()
df.unstack()
df.melt()

# Solution:

import pandas as pd

df = pd.DataFrame({"A": [1,