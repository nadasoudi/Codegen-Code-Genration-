import urllib.request

url = "https://www.python.org/ftp/python/3.8.5/python-3.8.5.tgz"

with urllib.request.urlopen(url) as response:
    data = response.read()
    print(data.decode('utf-8'))
    print(data.decode('utf-8').split('\n')[0])