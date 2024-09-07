def count_elements(lst):
    count = {}
    for i in lst:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(count_elements(lst))

"""

# Solution:

def count_elements(lst):