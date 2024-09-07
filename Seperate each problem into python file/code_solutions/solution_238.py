import re

html = """
<html>
<head>
<title>First Head Title</title>
</head>
<body>
<p>First Head Title</p>
<p>Second Head Title</p>
<p>Third Head Title</p>
</body>
</html>
"""

# Solution:

# regex = re.compile(r'<a href="(.*?)">')
# result = regex.find