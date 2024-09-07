def removeDuplicate(d):
    newDict = {}
    for key in d:
        if d[key] not in newDict:
            newDict[d[key]] = 1
        else:
            newDict[d[key]] += 1
    return newDict

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(removeDuplicate(d))

"""

"""