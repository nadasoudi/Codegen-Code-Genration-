def count_float(mixed_list):
    return sum(map(lambda x: isinstance(x, float), mixed_list))

print(count_float([1, 2.0, 'a', [1, 2]]))

"""

def count_float(mixed_list):
    return sum(map(lambda x: isinstance(x, float), mixed_list))

print(count_float([1, 2.0, 'a', [1, 2