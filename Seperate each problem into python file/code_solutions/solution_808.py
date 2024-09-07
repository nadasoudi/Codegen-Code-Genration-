import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0, 100, size=(10, 4)), columns=['col1', 'col2', 'col3', 'col4'])
print(df)

df.max()

df.max(axis=1)

df.max(axis=1).max()

df.max(axis=