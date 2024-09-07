import pandas as pd

df = pd.read_csv('https://github.com/jbrownlee/Datasets/blob/master/data/fips_code_data.csv?raw=true')
df['fips'] = df['fips'].astype(str)
df['fips'] = df['fips'].str.zfill(5)
df['year'] = df['fips'].str[: