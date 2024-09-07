def common_elements(l1, l2):
    l1.sort()
    l2.sort()
    if l1 == l2:
        return True
    else:
        return False

l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4, 5, 6]
print(common_elements(l1, l2))

"""

# Solution:

def common_e