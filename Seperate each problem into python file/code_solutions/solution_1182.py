def get_string(n):
    return "".join(random.choice(string.ascii_letters) for i in range(n))

print(get_string(5))

"""

# Solution:

def get_string(n):
    return "".join(random.choice(string.ascii_letters) for i in range(n))

print(get_string(5))