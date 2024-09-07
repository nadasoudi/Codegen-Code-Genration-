df = pd.DataFrame({'Customer ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                   'Monthly Purchase Amount': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]})

df.groupby('Monthly Purchase Amount').sum()

df.groupby('Monthly Purchase Amount').sum().plot(kind='bar')

df.groupby('Monthly Purchase Amount