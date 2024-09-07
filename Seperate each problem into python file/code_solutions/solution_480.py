import pandas as pd

# Read the data
df = pd.read_csv('/Users/srinivasan/Downloads/airline_data.csv')

# Create a new dataframe with only the columns that are required
df_new = df[['Origin','Destination','Reporting_Airline','Reporting_Airline_Code','Reporting_Airline_Name','Reporting_Airline_State','Reporting_Airline_Country','Reporting_Air