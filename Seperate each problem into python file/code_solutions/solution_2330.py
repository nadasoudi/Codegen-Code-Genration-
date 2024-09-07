def sort_string(string1, string2):
    if string1 > string2:
        return string2
    elif string1 < string2:
        return string1
    else:
        return string1

print(sort_string("a", "b"))
print(sort_string("a", "c"))
print(sort_string("c", "b"))
print(sort_string("c", "a"))

"""

def sort_string(string1, string2):