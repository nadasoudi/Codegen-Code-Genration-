import itertools

def permutations(lst):
    if len(lst) == 1:
        return [lst]
    else:
        return list(itertools.permutations(lst))

print(permutations([1,2,3]))
print(permutations([1,2,3,4]))
print(permutations([1,2,3,4,5]))
print(permutations([1,2,3,4,5,