python solution.py

"""

import csv

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(f"CSV Header: {header_row}")
    for row in reader:
        print(row)