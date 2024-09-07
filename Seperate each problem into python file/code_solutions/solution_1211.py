def generate_sublists(lst):
    sublists = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            sublists.append([lst[i], lst[j]])
    return sublists

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(generate_sublists(lst))

"""

def generate_