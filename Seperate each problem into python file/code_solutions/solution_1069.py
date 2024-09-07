import pandas as pd

# Create a dataframe
df = pd.DataFrame({'Name': ['Rolf', 'Charlie', 'Anna', 'Bob', 'Jen', 'Sue'],
                   'Age': [30, 32, 33, 34, 35, 36],
                   'Salary': [55000, 60000, 50000, 50000, 50000, 50000]})

# Create a new column
df['Date'] = pd.to_datetime(df