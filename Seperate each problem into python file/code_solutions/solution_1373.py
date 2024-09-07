def count_chars(str,ch):
    count = 0
    for i in range(len(str)):
        if str[i] == ch:
            count += 1
    return count

print(count_chars("python", "P"))

"""

def count_chars(str,ch):
    count = 0
    for i in range(len(str)):
        if str[i] ==