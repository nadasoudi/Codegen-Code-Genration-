def count_positive_negative(list):
    count = 0
    for i in list:
        if i > 0:
            count += 1
        elif i < 0:
            count += 1
    return count

print(count_positive_negative([-1, -2, -3, -4, -5]))

"""

def count_positive_negative(list):
    count = 0
    for i in list:
        if i > 0:
            count += 1