import urllib.request

url = "https://www.en.wikipedia.org/wiki/Robot_%28s_%28s%29"

with urllib.request.urlopen(url) as response:
    data = response.read()
    print(data.decode("utf-8"))

"""

import urllib.request
import urllib.parse
import urllib.error

url = "https://