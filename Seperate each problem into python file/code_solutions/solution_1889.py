def test_substring_order(s):
    if len(s) == 0:
        return True
    if len(s) == 1:
        return False
    if s[0] == s[1]:
        return test_substring_order(s[2:])
    else:
        return test_substring_order(s[1:])

print(test_substring_order("abababababababababababababababababababababababab