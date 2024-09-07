import pandas as pd

employee = pd.read_excel('employee.xlsx')

employee.index = pd.to_datetime(employee.hire_date)

employee.index.name = 'Date'

print(employee)

# Solution:

# import pandas as pd
# import datetime as dt