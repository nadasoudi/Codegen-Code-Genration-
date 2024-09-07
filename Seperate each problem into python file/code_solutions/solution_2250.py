def sort_by_frequency(tuple_list):
    # your code goes here
    return sorted(tuple_list, key=lambda x: x[1])

tuple_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
print(sort_by_frequency(tuple_list))

"""

# Solution

def sort_by_frequency(tuple_list):
    # your code goes here