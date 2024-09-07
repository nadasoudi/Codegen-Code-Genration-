def get_items(list, condition):
    for item in list:
        if condition(item):
            yield item

print(get_items([1, 2, 3, 4, 5], lambda x: x % 2 == 0))

"""

def get_items(list, condition):
    for item in list:
        if condition(item):
            yield item

print(get_items([1, 2, 3, 4, 5], lambda x: x %