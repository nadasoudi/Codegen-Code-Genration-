import csv

with open('data.csv', 'r') as f:
    csv_reader = csv.reader(f)
    data = list(csv_reader)

data = data[1:]

for i in range(len(data)):
    data[i] = data[i][0].split(',')

print(data)

# Solution:

import csv

with open('data.csv',