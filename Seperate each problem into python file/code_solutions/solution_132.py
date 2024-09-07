import pandas as pd

df = pd.read_excel('coalpublic2013.xlsx')

df['Name'] = df['Name'].str.lower()

df['Name'] = df['Name'].str.replace(' ', '-')

df['Name'] = df['Name'].str.replace(' ', '-')

df['Name'] = df['Name'