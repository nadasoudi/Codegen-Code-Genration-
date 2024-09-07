import pandas as pd

df = pd.read_csv('https://github.com/jbrownlee/Datasets/blob/master/pima-indians-diabetes.csv?raw=true')

# Split the data into X and y
X = df.iloc[:, 0:8]
y = df.iloc[:, 8]

# Split the data into training and testing sets
from sklearn.model_selection import train_test_split
X_