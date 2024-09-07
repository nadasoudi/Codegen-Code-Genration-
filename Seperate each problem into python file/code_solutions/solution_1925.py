import csv

with open('data.csv', 'r') as f:
    csv_reader = csv.reader(f)
    data = list(csv_reader)

data.sort(key=lambda x: int(x[0]))

with open('sorted_data.csv', 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(data)

"""

import csv

with open('data