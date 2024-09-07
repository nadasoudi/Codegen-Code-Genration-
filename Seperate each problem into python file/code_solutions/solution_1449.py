import urllib.request
import re

url = "http://py4e-data.dr-chuck.net/known_by_Fikri.html"
html = urllib.request.urlopen(url).read()

# find all the <p> tags
p = re.compile(r'<p>(.*?)</p>')

# find all the <a> tags
a = re.compile(r'<a href="