import random

def random_selection(lst, n):
    """
    This function returns a list of n random elements from the given list.
    """
    return [lst[random.randint(0, len(lst) - 1)] for i in range(n)]

print(random_selection(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',