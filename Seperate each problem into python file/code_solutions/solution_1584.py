import urllib.request

url = "https://www.python.org/~guido/python-projects/python-projects.html"

with urllib.request.urlopen(url) as response:
    html = response.read()
    print(html.decode())

"""

import urllib.request

url = "https://www.python.org/~guido/python-projects/python-projects