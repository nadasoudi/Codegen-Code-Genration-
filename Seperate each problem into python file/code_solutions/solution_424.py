import csv

with open('solution.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows([{'first_name': 'John', 'last_name': 'Doe',