import csv

with open('data.csv', 'r') as f:
    csv_dict = csv.DictReader(f)
    for row in csv_dict:
        print(row)

"""

import csv

with open('data.csv', 'r') as f:
    csv_dict = csv.DictReader(f)
    for row in csv_dict:
        print(row)

"""

import csv