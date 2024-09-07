def longest_iterable(iterable):
    """
    >>> longest_iterable([1, 2, 3, 4, 5])
    4
    >>> longest_iterable([1, 2, 3, 4, 5, 6])
    6
    >>> longest_iterable([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    10
    """
    return max(iterable, key=len)