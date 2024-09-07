def max_min(set):
    max = set[0]
    min = set[0]
    for i in set:
        if i > max:
            max = i
        if i < min:
            min = i
    return max, min

set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(max_min(set))

"""

def max_min(set):
    max = set[0]
    min