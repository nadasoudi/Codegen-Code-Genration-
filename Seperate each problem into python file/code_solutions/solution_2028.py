import pandas as pd

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)

df.columns = ['sepal_length','sepal_width', 'petal_length', 'petal_width']

df['species'] = df['species'].map({'setosa': 0,'versicolor': 1, 'virginica': 2