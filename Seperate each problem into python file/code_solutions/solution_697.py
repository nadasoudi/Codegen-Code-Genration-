import pandas as pd

# Read the data
df = pd.read_csv('purch_amt.csv')

# Create a new dataframe with the columns customer_id, group, and purch_amt
df_grouped = df.groupby(['customer_id', 'group']).agg({'purch_amt': ['sum']})

# Create a new data