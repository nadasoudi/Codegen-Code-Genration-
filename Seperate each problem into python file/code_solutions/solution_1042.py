import urllib.request
import urllib.parse
import urllib.error

url = "http://py4e-data.dr-chuck.net/comments_42.html"

try:
    fhand = urllib.request.urlopen(url)
except urllib.error.URLError as e:
    print("ERROR:", e.reason)

for line in fhand:
    print(line.decode().