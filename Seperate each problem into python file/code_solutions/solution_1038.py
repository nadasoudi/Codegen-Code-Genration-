import collections

def unique_values(lst):
    d = collections.Counter(lst)
    return dict(d)

print(unique_values([1,2,3,4,5,6,7,8,9,10]))

# Output: {1: 2, 2: 1, 3: 2, 4: 2, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10