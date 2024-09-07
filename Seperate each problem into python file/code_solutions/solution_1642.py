def valid_ip(ip):
    if len(ip)!= 8:
        return False
    for i in range(0, len(ip)):
        if not ip[i].isdigit():
            return False
        if not ip[i].isalpha():
            return False
        if not ip[i].isupper():
            return False
        if not ip[i].islower():
            return False
        if not ip[i].isnumeric():
            return False
        if not ip