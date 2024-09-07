def bold(func):
    def wrapper(*args, **kwargs):
        return f'{func(*args, **kwargs)} {func.__name__}'
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        return f'{func(*args, **kwargs)} {func.__name__}'
    return wrapper

def underline(func):
    def wrapper(*args,