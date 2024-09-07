import sys

def get_module(obj):
    if isinstance(obj, str):
        return sys.modules[obj]
    elif isinstance(obj, int):
        return sys.modules[str(obj)]
    else:
        raise TypeError("Object is not a string or an int")

def get_module_name(obj):
    if isinstance(obj, str):
        return obj
    elif isinstance(obj, int):
        return str(