def is_user_defined_function(func):
    if type(func) == types.FunctionType:
        return True
    else:
        return False

print(is_user_defined_function(lambda x: x + 1))

"""

# Solution:

def is_user_defined_function(func):
    if type(func) == types.FunctionType:
        return True
    else: