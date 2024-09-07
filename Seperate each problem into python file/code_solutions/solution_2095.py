import csv

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

# To sort the file by multiple columns
file_data.sort(key=lambda x: (x[3], x[5], x[2]))

# To print the first 5 rows
print(file_data[:5])

# To print the last 5 rows
print(file_data[-5:])