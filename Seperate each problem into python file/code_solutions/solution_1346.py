import json

def is_complex(json_string):
    try:
        json.loads(json_string)
    except ValueError:
        return False
    else:
        return True

print(is_complex("{'a': 1, 'b': 2}"))
print(is_complex("[1, 2, 3]"))
print(is_complex("[1, 2, 3, 4]"))
print(is_complex("[1, 2, 3,