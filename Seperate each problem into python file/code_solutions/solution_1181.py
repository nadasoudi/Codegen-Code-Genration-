def get_id(web_page):
    for i in range(len(web_page)):
        if web_page[i] == '<':
            return i

print(get_id('<html><body><h1>Hello</h1></body></html>'))

"""

def get_id(web_page):
    for i in range(len(web_page)):
        if web_page[i] ==