def first_non_repeating_char(string):
    # your code goes here
    for i in range(len(string)):
        if string[i] == string[i+1]:
            return string[i]
    return''

print(first_non_repeating_char('abcabcbb'))
print(first_non_repeating_char('bbbbb'))
print(first_non_repeating_char('pwwkew'))