import pandas as pd

df = pd.read_csv('world_alcohol_consumption.csv')

df['year'] = df['year'].astype(int)

df.head()

df.columns = ['year', 'country', 'country_code', 'country_name', 'country_code_name', 'country_name_code', 'country_name_code_name', 'country_name_code_name_code