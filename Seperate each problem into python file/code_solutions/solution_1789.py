def check_url(url):
    if 'http' in url:
        return True
    else:
        return False

print(check_url('http://google.com'))
print(check_url('http://www.google.com'))
print(check_url('http://www.google.com'))
print(check_url('http://www.google.com'))
print(check_url('http://www.google.com'))
print(check_url('http://www