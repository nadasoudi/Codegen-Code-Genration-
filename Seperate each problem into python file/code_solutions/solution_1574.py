import pandas as pd

df = pd.read_excel('coalpublic2013.xlsx')

df = df[df['MSHA_ID'].isin(['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',