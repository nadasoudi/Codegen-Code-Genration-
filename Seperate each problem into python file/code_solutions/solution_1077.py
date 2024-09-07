def get_max_min(d):
    max_val = d[0]
    min_val = d[0]
    for i in d:
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i
    return max_val, min_val

d = {1: 10, 2: 20, 3: 30}
print(get_max_min(d))

"""

def