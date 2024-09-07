def combinations(lst, condition):
    if condition == 0:
        return [''.join(i) for i in itertools.permutations(lst)]
    elif condition == 1:
        return [''.join(i) for i in itertools.combinations(lst, 2)]
    elif condition == 2:
        return [''.join(i) for i in itertools.combinations(lst, 3)]
    elif condition == 3: