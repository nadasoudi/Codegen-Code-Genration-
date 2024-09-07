import csv

with open('timestamp.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Name', 'Age', 'Job', 'Salary'])
    csvwriter.writerow(['John', 25, 'Engineer', 2000])
    csvwriter.writerow(['Anna', 30, 'Data Scientist', 30000])
    csvwriter.writerow(['Peter', 40, 'Data Scientist', 40000])
    csvwriter