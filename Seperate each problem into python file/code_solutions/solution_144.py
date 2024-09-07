import re

# create a regex pattern
pattern = r'<[^>]+>'

# create a regex object
regex = re.compile(pattern)

# create a regex object
regex2 = re.compile(pattern, re.DOTALL)

# create a regex object
regex3 = re.compile(pattern, re.MULTILINE)

# create a regex object
regex4 = re.comp