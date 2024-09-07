def max_aggregate(pairs):
    max_aggregate = 0
    for pair in pairs:
        if max_aggregate < pair[1]:
            max_aggregate = pair[1]
    return max_aggregate

print(max_aggregate([(1, 2), (3, 4), (5, 6)]))

"""

# Solution:

def max_aggregate(pairs):
    max_aggregate = 0