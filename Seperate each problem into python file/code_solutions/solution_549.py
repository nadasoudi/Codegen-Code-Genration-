def is_list(var):
    if type(var) == list:
        return True
    else:
        return False

def is_tuple(var):
    if type(var) == tuple:
        return True
    else:
        return False

def is_set(var):
    if type(var) == set:
        return True
    else:
        return False

def is_list_or_tuple_or_set(var