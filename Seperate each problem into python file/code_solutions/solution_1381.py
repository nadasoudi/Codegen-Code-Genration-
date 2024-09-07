import pandas as pd

df = pd.read_excel('coalpublic2013.xlsx')

df.plot(kind='bar', figsize=(10,10))

# Create a bar plot with the top 10 production

df.plot(kind='bar', figsize=(10,10), rot=0)

# Create a bar plot with the top 10 production