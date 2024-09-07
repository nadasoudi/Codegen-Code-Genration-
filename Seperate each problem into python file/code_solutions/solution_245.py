import urllib.request
import re

url = "http://py4e-data.dr-chuck.net/known_by_Fikri.html"
html = urllib.request.urlopen(url).read()

print(html)

# Extract the text from the URL

text = re.findall(r'<p>(.*?)</p>', html)

print(text)