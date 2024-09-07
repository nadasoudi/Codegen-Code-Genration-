import urllib.request

url = "http://www.google.com"
querystring = "?q=http%3A%2F%2Fwww.google.com"

with urllib.request.urlopen(url + querystring) as response:
    print(response.read().decode())

"""

import urllib.request
import urllib.parse

url = "http://www.google.com"
querystring = "