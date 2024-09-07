import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('coalpublic2013.xlsx')
df.head()

df.columns = ['Year', 'MSHA_ID', 'Production', 'Labor_hours']
df.head()

df.head()

df.head()