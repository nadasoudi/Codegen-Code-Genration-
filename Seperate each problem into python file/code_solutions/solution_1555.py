def split_iter(iterable, n):
    """Split an iterable into n iterables.

    >>> split_iter(range(10), 3)
    [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    >>> split_iter(range(10), 4)
    [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9]]
    """
    return [iter(iter