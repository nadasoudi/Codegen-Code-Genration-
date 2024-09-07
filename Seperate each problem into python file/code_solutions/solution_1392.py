import urllib.request
import html

url = "http://py4e-data.dr-chuck.net/known_by_Fikri.html"
html = urllib.request.urlopen(url).read()
print(html)

# Solution:

# import urllib.request
# import html

# url = "http://py4e-data.dr-chuck.net/known_by_F