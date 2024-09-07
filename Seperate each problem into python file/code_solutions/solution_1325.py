def count_upper(string):
    count = 0
    for i in string:
        if i.isupper():
            count += 1
    return count

def count_lower(string):
    count = 0
    for i in string:
        if i.islower():
            count += 1
    return count

def count_special(string):
    count = 0
    for i in string:
        if i.isdigit():