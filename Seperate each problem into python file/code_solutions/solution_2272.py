import csv

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    file_data = list(reader)

# To remove the header from the data
file_data.pop(0)

# To convert the data into a list
data = []
for row in file_data:
    data.append(row)

# To print the data
print(data)

# To create a new CSV file
with open