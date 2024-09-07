def index(list, item):
    for i in range(len(list)):
        if list[i] == item:
            return i
    return -1

print(index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))

"""

def index(list, item):
    for i in range(len(list)):
        if list[i] == item:
            return i
    return -1