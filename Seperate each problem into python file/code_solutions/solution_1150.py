def max_consecutive_zeroes(binary_string):
    max_len = 0
    for i in range(len(binary_string)):
        if binary_string[i] == '0':
            if i == 0 or binary_string[i-1] == '0':
                max_len += 1
            else:
                max_len = max(max_len, i-1)
    return max_len

print(max_consecutive