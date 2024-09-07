def convert_snake_case(s):
    return s.title()

print(convert_snake_case("SNAKE_CASE"))

"""

# Solution 1

def convert_snake_case(s):
    return s.title()

print(convert_snake_case("SNAKE_CASE"))

# Solution 2

def convert_snake_case(s):
    return s.title().replace("_", " ").replace("-",