import pandas as pd

employee = pd.read_excel('employee.xlsx')

employee_list = employee.loc[(employee['hire_date'] >= '2021-01-01') & (employee['hire_date'] <= '2021-12-31')]

print(employee_list)

# Solution: