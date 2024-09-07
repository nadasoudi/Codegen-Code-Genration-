import itertools

def find_pairs(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] * lst[j] == lst[i] * lst[j]:
                print(lst[i], lst[j])

find_pairs([1, 2, 3, 4, 5, 6