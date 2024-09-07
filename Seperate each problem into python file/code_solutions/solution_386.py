import csv

with open('data.csv', 'r') as f:
    csv_reader = csv.reader(f)
    file_data = list(csv_reader)

file_data.pop(0)

numbers = []

for i in range(len(file_data)):
    numbers.append(int(file_data[i][1]))

numbers.sort()

print(numbers)

# Solution