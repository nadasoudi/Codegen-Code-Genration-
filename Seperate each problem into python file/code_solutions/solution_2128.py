def min_subsets(arr):
    count = Counter(arr)
    return count.most_common(1)[0][1]

print(min_subsets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

"""

def min_subsets(arr):
    count = Counter(arr)
    return count.most_common(1)[0][1]

print(min_subsets([1, 2, 3, 4