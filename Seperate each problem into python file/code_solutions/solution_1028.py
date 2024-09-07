import urllib.request
import bs4

url = "https://www.python.org/blogs/html-tables/"
html = urllib.request.urlopen(url)
soup = bs4.BeautifulSoup(html, 'html.parser')

# print(soup.prettify())

# print(soup.prettify())

# print(