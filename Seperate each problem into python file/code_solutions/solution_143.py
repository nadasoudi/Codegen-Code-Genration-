import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4), columns=['a', 'b', 'c', 'd'])

print(df)

# Create a heatmap
import matplotlib.pyplot as plt
import seaborn as sns

sns.heatmap(df.corr(), annot=True)