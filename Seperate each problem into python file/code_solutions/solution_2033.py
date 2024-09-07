import urllib.request
import re

url = "http://www.python.org/~guido/python-exercises/"

# Open the URL
webpage = urllib.request.urlopen(url)

# Read the HTML
data = webpage.read()

# Parse the HTML
soup = BeautifulSoup(data, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')

# Loop over the tags
for tag