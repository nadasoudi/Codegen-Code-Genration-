import json
import csv

with open('solution.json') as f:
    data = json.load(f)

with open('solution.csv', 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['name', 'age', 'gender'])
    for person in data:
        csv_writer.writerow([person['name'], person['age'], person['gender']])

"""

import json
import csv