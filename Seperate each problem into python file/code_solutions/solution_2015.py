import pandas as pd

df = pd.read_csv('https://github.com/jbrownlee/Datasets/blob/master/iris.csv?raw=true')

df.columns = ['sepal_length','sepal_width', 'petal_length', 'petal_width']

df.head()

df.columns = ['sepal_length','sepal_width', 'petal_length', 'petal_width']