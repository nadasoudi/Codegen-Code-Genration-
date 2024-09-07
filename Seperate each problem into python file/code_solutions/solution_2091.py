import pandas as pd

df = pd.read_csv('https://github.com/jbrownlee/Datasets/blob/master/pima-indians-diabetes.csv?raw=true')

df.head()

df.columns = ['age','sex', 'bmi', 'bp','s1','s2','s3','s4','s5','s6']

df.head()

df.columns =