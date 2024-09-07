import itertools

def combinations(lst, n):
    """
    :param lst: list
    :param n: number of elements
    :return: list of all possible combinations
    """
    return list(itertools.combinations(lst, n))

print(combinations([1, 2, 3, 4, 5], 2))

"""
Output:
[(1, 2, 3, 4, 5), (1,