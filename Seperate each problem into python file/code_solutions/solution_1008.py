import urllib.request

url = "https://en.wikipedia.org/wiki/Main_Page"

with urllib.request.urlopen(url) as response:
    html = response.read()
    print(html)

# Extracting the header tags

import re

url = "https://en.wikipedia.org/wiki/Main_Page"

with urllib.request.urlopen(url) as