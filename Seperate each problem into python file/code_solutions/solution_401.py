import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0, 100, size=(10, 4)), columns=['col1', 'col2', 'col3', 'col4'])
df['col5'] = df['col1'] > 0.5
df.head()

# Solution:

# Create a