import csv

with open('test.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age', 'Class'])
    writer.writerow(['John', 25, 'First'])
    writer.writerow(['Anna', 27, 'Second'])
    writer.writerow(['Peter', 29, 'Third'])