def local_vars(func):
    def wrapper(*args, **kwargs):
        print("Number of local variables: ", len(args))
        return func(*args, **kwargs)
    return wrapper

@local_vars
def add(a, b):
    return a + b

print(add(1, 2))

"""

# Solution 2

def local_vars(func):
    def wrapper(*args, **kwargs):
        print