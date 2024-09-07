def check_substring(string, sub_string):
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            return True
    return False

print(check_substring("abcd", "ab"))
print(check_substring("abcd", "abcd"))
print(check_substring("abcd", "abcdab"))
print(check_substring("abcd