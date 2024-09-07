def check_consecutive(lst):
    for i in range(len(lst)):
        if lst[i] == lst[i+1] and lst[i] == lst[i+2]:
            return True
    return False

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(check_consecutive(lst))

"""

# Solution 1

def check_