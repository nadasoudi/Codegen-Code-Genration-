import csv

with open('data.csv', 'r') as f:
    csv_reader = csv.reader(f)
    data = list(csv_reader)

print(data)

# Solution:

# import csv
#
# with open('data.csv', 'r') as f:
#     csv_reader = csv.reader(f)
#     data = list(csv_reader)
#
# print(data)

# Solution:

#