df = pd.DataFrame({'Date': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                   'Amount': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200]})

df.groupby('Date').sum()

df.groupby('Date').sum().plot()

df.group