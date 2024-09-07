# Import pandas
import pandas as pd

# Read the data
titanic = pd.read_csv('titanic.csv')

# Print the dataframe
print(titanic)

# Print the first five rows of the dataframe
print(titanic.head())

# Print the shape of the dataframe
print(titanic.shape)

# Print the column names of the dataframe
print(titanic.