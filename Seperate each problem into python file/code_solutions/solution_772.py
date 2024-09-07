import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/student_scores.csv')

df['Tag'] = df['Name'].str.extract('(\w+)')

df.head()

df.Tag.value_counts()

df.Tag.value_counts().sort_index()

df.Tag.value_counts().