def shift_last_element(lst):
    lst.pop()
    lst.pop()
    lst.append(lst.pop(0))
    lst.insert(0,lst.pop(0))
    return lst

lst = [1,2,3,4,5,6,7,8,9,10]
print(shift_last_element(lst))

"""

def shift_