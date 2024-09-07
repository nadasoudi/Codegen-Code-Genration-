def add_strings(a, b):
    if type(a) == str and type(b) == str:
        return a + b
    else:
        return "Numbers must be strings"

print(add_strings(1, 2))
print(add_strings("1", "2"))
print(add_strings(1, "2"))
print(add_strings(1, "2"))
print(add_strings(