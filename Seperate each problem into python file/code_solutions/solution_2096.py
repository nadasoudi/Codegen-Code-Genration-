def extract_symmetric_tuples(lst):
    return tuple(sorted(lst, key=lambda x: x[0]))

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(extract_symmetric_tuples(lst))

"""

# Solution:

def extract_symmetric_tuples(lst):
    return tuple(sorted(lst, key=lambda x: x[