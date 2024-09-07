import pandas as pd
import datetime as dt

# Read the data from the csv file
df = pd.read_csv('data.csv')

# Create a new dataframe with the data
df_new = df.copy()

# Create a new column named 'business_day'
df_new['business_day'] = df_new['date'].dt.day_name