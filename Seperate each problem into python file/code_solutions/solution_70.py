def check_dict(d):
    for key in d:
        if d[key]!= d[key]:
            return False
    return True

print(check_dict({1:1, 2:2, 3:3, 4:4, 5:5}))

"""

def check_dict(d):
    for key in d:
        if d[key]!= d[key]:
            return False
    return True

print(check_dict({1:1