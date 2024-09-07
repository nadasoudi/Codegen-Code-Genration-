def count_digits(string):
    count = 0
    for i in string:
        if i.isdigit():
            count += 1
    return count

print(count_digits("Python is easy to learn"))

"""

def count_digits(string):
    count = 0
    for i in string:
        if i.isdigit():
            count += 1
    return count

print(count_digits("Python is easy to learn