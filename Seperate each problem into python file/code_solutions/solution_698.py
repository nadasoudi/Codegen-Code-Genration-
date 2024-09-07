import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/blogs/html-tables/"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# print(soup.prettify())

# print(soup.title)
# print(soup.title.string)
# print(soup.title.name)
# print(soup