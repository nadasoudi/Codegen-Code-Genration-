import numpy as np
import matplotlib.pyplot as plt

np.random.laplace(loc=0, scale=1, size=100)

"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, [2, 3]].values
y =