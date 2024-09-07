def all_equal(lst):
    for i in lst:
        if lst.count(i)!= 1:
            return False
    return True

lst = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",