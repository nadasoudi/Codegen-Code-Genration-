import csv

with open('data.csv', 'r') as f:
    csv_reader = csv.reader(f)
    file_data = list(csv_reader)

file_data.pop(0)

new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

new_data.sort()

print(new_data)