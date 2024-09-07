import re

html = '''
<html>
<head>
<title>First Title</title>
</head>
<body>
<p>First paragraph.</p>
<p>Second paragraph.</p>
<p>Third paragraph.</p>
</body>
</html>
'''

# Solution:

# Solution 1:
# regex = re.compile(r'<a.*?>')
# result = regex.find