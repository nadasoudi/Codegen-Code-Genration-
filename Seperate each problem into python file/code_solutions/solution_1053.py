import urllib.request
import re

url = "https://python.org/"

# Open the url
webpage = urllib.request.urlopen(url)

# Read the webpage
html = webpage.read()

# Find all the links
links = re.findall(r'<a href="(.*?)">', html)

# Print the first ten links
for link in links[:10]:
    print(link)