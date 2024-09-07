import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0, 100, size=(10, 4)), columns=['col1', 'col2', 'col3', 'col4'])
print(df)

df.loc[:, 'col1'] = np.random.randint(0, 100, size=10)
print(df)

df.