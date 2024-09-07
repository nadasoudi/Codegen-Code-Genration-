import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4), columns=['a', 'b', 'c', 'd'])

# Create a new column named 'color' with a random value from the 'a' column.
df['color'] = np.random.randint(0, 4, size=len(df))

# Create