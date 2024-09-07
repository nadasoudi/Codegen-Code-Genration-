def max_substring(string):
    max_substring = 0
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i:j+1] not in string:
                if string[i:j+1] > max_substring:
                    max_substring = string[i:j+1]
    return max_substring

print(max_substring("abcdefghijklmnopqrstuvw