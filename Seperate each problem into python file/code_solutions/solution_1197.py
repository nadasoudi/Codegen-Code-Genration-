import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/blogs/python-web-scraping/p/python-web-scraping-with-beautifulsoup-and-selenium-in-python-3"

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

print(soup.prettify())

# print(soup.pre