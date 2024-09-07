def count_upper_lower(string):
    count = 0
    for i in string:
        if i.isupper():
            count += 1
    return count

print(count_upper_lower("Python is fun"))

"""

def count_upper_lower(string):
    count = 0
    for i in string:
        if i.isupper():
            count += 1
    return count

print(count_upper_lower("Python