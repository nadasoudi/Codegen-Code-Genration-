def flatten(lst):
    # your code goes here
    flattened = []
    for i in lst:
        if type(i) == list:
            flattened.extend(flatten(i))
        else:
            flattened.append(i)
    return flattened

lst = [[1,2,3],[4,5,6],[7,8,9]]
print(flatten(lst))

"""

def flatten(l