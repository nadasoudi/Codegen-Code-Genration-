import re

url = "https://www.example.com"

# find all h1 tags
h1_tags = re.findall(r'<h1>(.+?)</h1>', url)

# extract h1 tag
h1_tag = h1_tags[0]

print(h1_tag)

# find all h2 tags
h2_tags = re.findall(r'<h2>(.+?)</h2>', url