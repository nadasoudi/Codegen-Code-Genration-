import datetime

def date_converter(date):
    return datetime.datetime.strptime(date, '%d-%m-%Y').strftime('%Y-%m-%d')

print(date_converter('2021-01-01'))

"""

# Solution 1

import datetime

def date_converter(date):
    return datetime.datetime.strptime(date, '