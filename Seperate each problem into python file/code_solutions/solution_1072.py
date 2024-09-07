import pandas as pd

# Read the data from the file
df = pd.read_csv('phone_number.csv')

# Extract the phone number from the column
phone_number = df['phone_number']

# Print the phone number
print(phone_number)

# Create a new column in the DataFrame called 'phone_number_extracted'
df['phone_number_extracted'] = phone_number.str.extract('(\