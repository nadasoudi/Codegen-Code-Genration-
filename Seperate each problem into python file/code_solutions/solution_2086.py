def check_variable(variable):
    if variable in globals():
        return True
    else:
        return False

print(check_variable("variable"))

"""

# Solution

def check_variable(variable):
    if variable in globals():
        return True
    else:
        return False

print(check_variable("variable"))