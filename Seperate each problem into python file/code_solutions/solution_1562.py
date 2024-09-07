import itertools

def permutations(elements, values):
    if len(elements) == 0:
        return []
    if len(elements) == 1:
        return [elements]
    
    result = []
    for i in range(len(values)):
        for j in itertools.combinations(elements, i + 1):
            result.append(j)
    return result

print(permutations(['a', 'b',