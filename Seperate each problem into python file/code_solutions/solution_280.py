def split_values(values, filter_list):
    result = []
    for value in values:
        if filter_list.count(value) > 0:
            result.append(value)
    return result

print(split_values([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""

def split_values