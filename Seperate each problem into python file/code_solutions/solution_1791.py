import pandas as pd

df = pd.read_csv('https://github.com/jbrownlee/Datasets/blob/master/pima-indians-diabetes.csv?raw=true')

df['Gender'] = df['Sex'].map({'female': 0,'male': 1})
df['Age'] = df['Age'].fillna(df['Age'].median())
df['EstimatedSalary'] = df['Age'] * df['BMI']