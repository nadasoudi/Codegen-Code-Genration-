df = pd.DataFrame({'col1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                   'col2': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]})

df.groupby(['col1']).agg({'col2': ['sum']})

df.groupby(['col1', 'col2']).