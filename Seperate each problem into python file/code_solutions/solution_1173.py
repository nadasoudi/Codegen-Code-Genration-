def add_prefix(string, prefix):
    return prefix.join(string.splitlines())

print(add_prefix("Hello World", "Hello"))

"""

def add_prefix(string, prefix):
    return prefix.join(string.splitlines()) + " "

print(add_prefix("Hello World", "Hello"))