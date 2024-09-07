import pandas as pd

employee = pd.read_excel('employee.xlsx')

employee_list = employee.values.tolist()

for employee in employee_list:
    if employee[3] > '01-01-07':
        print(employee)

# Solution:

import pandas as pd