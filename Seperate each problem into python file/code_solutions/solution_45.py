import pandas as pd

# Read the data from the file
df = pd.read_csv("data.csv")

# Create a dictionary to store the data
dictionary = {'Word': df['Word'], 'Count': df['Count']}

# Create a dataframe from the dictionary
df = pd.DataFrame(dictionary)

# Print the dataframe
print(df)

# Create a function to calculate the number of characters in each