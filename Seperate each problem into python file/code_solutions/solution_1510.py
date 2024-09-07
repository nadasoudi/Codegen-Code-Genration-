import pandas as pd

# Read the data from the csv file
df = pd.read_csv('business_quaterly_data.csv')

# Create a new dataframe with the business quarter dates
business_quarter_dates = df[['Business quarter', 'Business quarter date']]

# Create a new dataframe with the business quarter dates
business_quarter_dates_new = business_quarter_dates.groupby(['Business quarter']).agg