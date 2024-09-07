def consecutive_char_frequency(string):
    count = 0
    for i in range(len(string)):
        if string[i] == string[i+1]:
            count += 1
    return count

print(consecutive_char_frequency("abcdefghijklmnopqrstuvwxyz"))

"""

def consecutive_char_frequency(string):
    count = 0
    for i in range(len(string)):
        if string[i] == string[i