import csv

with open('data.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        print(row)

# Solution:

# import csv
#
# with open('data.csv', 'r') as f:
#     csv_reader = csv.reader(f)
#     for row in csv_reader:
#         print