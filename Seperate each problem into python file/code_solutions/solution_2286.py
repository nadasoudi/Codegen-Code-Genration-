def get_parameters(func):
    parameters = func.__code__.co_varnames
    return parameters

def get_parameters(func):
    parameters = func.__code__.co_argcount
    return parameters

def get_parameters(func):
    parameters = func.__code__.co_kwonlyargcount
    return parameters

def get_parameters(func):
    parameters = func.__code__.co_kwonlyargcount