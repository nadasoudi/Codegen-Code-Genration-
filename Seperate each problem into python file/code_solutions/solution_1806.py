def get_subsets(set, size):
    if size == 0:
        return [[]]
    else:
        return [subset + [set[i]] for i in range(size)]

def get_subsets_recursive(set, size, subset):
    if size == 0:
        return [[]]
    else:
        if len(subset) == size:
            return [subset + [set[i]] for i in range(size)]
        else: