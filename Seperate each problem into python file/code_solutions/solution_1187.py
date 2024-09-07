def count_occurrence(string, char):
    count = 0
    for i in string:
        if i == char:
            count += 1
    return count

print(count_occurrence("Python", "P"))

"""

def count_occurrence(string, char):
    count = 0
    for i in string:
        if i == char:
            count += 1
    return count

print(count_occurrence("Python", "P"))