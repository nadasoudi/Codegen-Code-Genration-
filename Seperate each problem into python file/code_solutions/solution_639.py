python3 powerset.py

"""

def powerset(iterable):
    """
    :type iterable: Iterable
    :rtype: Iterator
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

print(powerset([1,2,3,4,5]))
print(powerset([1,2,3,4,5,