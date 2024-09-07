def check_order(string):
    d = OrderedDict()
    for i in string:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d

print(check_order("abcd"))

"""

def check_order(string):
    d = OrderedDict()
    for i in string:
        if i not in d:
            d[i] = 1