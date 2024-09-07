>>> import zipfile
>>> import os
>>> import sys
>>> import time
>>> import csv

>>> def read_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        return data

>>> def write_csv(filename, data):
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)

>>>