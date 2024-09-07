import csv

with open('data.csv', 'r') as csvfile:
    readCSV = csv.reader(csvfile)
    data = list(readCSV)

print(data)

# Solution:

# import csv
#
# with open('data.csv', 'r') as csvfile:
#     readCSV = csv.reader(csvfile)
#     data = list(readCSV)
#
# print(data)

#