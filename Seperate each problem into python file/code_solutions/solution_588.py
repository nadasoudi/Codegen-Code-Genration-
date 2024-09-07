def max_substring(str):
    max_len = 0
    for i in range(len(str)):
        for j in range(i, len(str)):
            if str[i:j+1] == str[i:j+1][::-1]:
                if len(str[i:j+1]) > max_len:
                    max_len =