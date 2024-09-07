import pandas as pd

# Create a dictionary to map the column names to the values
column_mapping = {
    'Name': 'Name',
    'Age': 'Age',
    'Gender': 'Gender',
    'DOB': 'DOB',
    'Job': 'Job',
    'Salary': 'Salary'
}

# Create a dataframe from the dictionary
df = pd.DataFrame(column_mapping, columns=['Name', 'Age', '