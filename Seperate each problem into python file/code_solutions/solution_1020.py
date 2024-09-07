import re

def wrap(element, tag):
    return f'<{tag}>{element}</{tag}>'

print(wrap('<b>Hello</b>', 'b'))
print(wrap('<b>Hello</b>', 'i'))
print(wrap('<b>Hello</b>', 'i'))
print(wrap('<b>Hello</b>', 'i'))
print(wrap('<b>Hello</