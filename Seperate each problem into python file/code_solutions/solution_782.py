import re

text = '''
This is a multi-line string.

This is also a multi-line string.

This is also a multi-line string.

'''

# Solution:
# Solution 1:
# text = re.sub('\n','', text)
# print(text)

# Solution 2:
# text = re.sub('\n','', text, 0, re.MULTILINE)
# print(