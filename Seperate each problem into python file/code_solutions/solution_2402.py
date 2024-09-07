import csv

with open('numbers.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

"""

import csv

with open('numbers.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

"""

"""

import csv

with open('numbers.csv', '