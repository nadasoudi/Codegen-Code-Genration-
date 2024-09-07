import re

def web_content(url):
    with open(url, 'r') as f:
        content = f.read()
    return content

def web_content_re(url):
    with open(url, 'r') as f:
        content = f.read()
    return re.findall(r'<a href="(.*?)">', content)

def web_content_re_2(url):
    with open(