import pandas as pd

# Read the data from the file
df = pd.read_csv("https://github.com/datasets/csv/blob/master/weather_data.csv?raw=true")

# Create a dataframe with the data
df_weather = df.copy()

# Select the columns we want to use
df_weather = df_weather[['date', 'temp', '