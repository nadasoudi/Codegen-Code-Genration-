def lowercase_first_n_chars(string, n):
    return string[:n].lower() + string[n:]

"""

def lowercase_first_n_chars(string, n):
    return string[:n].lower() + string[n:]

if __name__ == '__main__':
    string = "hello world"
    n = 3
    print(lowercase_first_n_chars(string, n))