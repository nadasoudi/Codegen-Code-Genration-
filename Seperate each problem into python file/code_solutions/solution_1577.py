import urllib.request
import urllib.parse
import urllib.error

url = "http://data.pr4e.org/romeo.txt"

try:
    fhand = urllib.request.urlopen(url)
except urllib.error.URLError as e:
    if hasattr(e, "code"):
        print("Error code