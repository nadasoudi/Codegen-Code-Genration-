# Import pandas
import pandas as pd

# Read the data
dataset = pd.read_csv('datasets/Alcohol_Consumption.csv')

# Create a new column 'Alcohol_Consumption'
dataset['Alcohol_Consumption'] = dataset['Alcohol_Consumption'].apply(lambda x: x if x >= 0 else 0)

# Create a new column 'Alcohol_Consumption'
dataset