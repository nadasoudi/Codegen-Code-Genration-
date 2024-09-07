def max_occuring_char(string):
    max_occuring_char = 0
    for i in string:
        if i == max_occuring_char:
            continue
        else:
            max_occuring_char = i
    return max_occuring_char

print(max_occuring_char("abcdefghijklmnopqrstuvwxyz"))

"""

def max_occuring_char(string):
    max_occuring