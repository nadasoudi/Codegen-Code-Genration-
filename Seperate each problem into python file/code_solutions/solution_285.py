def count_items(dictionary):
    count = 0
    for i in dictionary.values():
        count += len(i)
    return count

dictionary = {'a': ['b', 'c'], 'b': ['d', 'e'], 'c': ['f', 'g'], 'd': ['h', 'i'], 'e': ['j', 'k'], 'f': ['l','m'], 'g': ['n', 'o'