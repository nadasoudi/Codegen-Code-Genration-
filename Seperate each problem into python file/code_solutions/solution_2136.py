def max_k(tup):
    max_k = []
    for i in range(len(tup)):
        if tup[i] > max_k[-1]:
            max_k.append(tup[i])
        else:
            max_k.append(tup[i])
    return max_k

def min_k(tup):
    min_k = []
    for i in range(len(tup)):
        if tup