def is_present(str, lst):
    for i in lst:
        if i in str:
            return True
    return False

print(is_present("abc", ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",