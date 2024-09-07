df = pd.DataFrame({'value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'group': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']})

df.groupby('group').count()

df.groupby('group').agg({'value': 'count'})

df.groupby('group').