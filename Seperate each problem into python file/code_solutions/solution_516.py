import pandas as pd

# Read the data
df = pd.read_csv('https://github.com/jbrownlee/Datasets/blob/master/pima-indians-diabetes.csv?raw=true')

# Replace missing values
df.fillna(df.median(), inplace=True)

# Print the dataframe
print(df)

# Create a new column called 'Class'