def count_common_char(str):
    count = 0
    for i in str:
        if i in str:
            count += 1
    return count

print(count_common_char("abcdefghijklmnopqrstuvwxyz"))

"""

def count_common_char(str):
    count = 0
    for i in str:
        if i in str:
            count += 1
    return count

print(count_common