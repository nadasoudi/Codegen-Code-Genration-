import csv

with open('solution.csv', 'w', newline='') as solution:
    solution_writer = csv.writer(solution)
    solution_writer.writerow(['Name', 'Age', 'Salary'])
    solution_writer.writerow(['John', '25', '$100'])
    solution_writer.writerow(['Anna', '25', '