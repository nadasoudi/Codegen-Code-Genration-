import csv

with open('data.csv', 'r') as f:
    csv_reader = csv.reader(f)
    print(type(csv_reader))
    print(csv_reader)
    print(csv_reader[0])
    print(csv_reader[0][0])
    print(csv_reader[0][1])
    print(csv_reader[0][2])
    print(csv_reader[0][3])