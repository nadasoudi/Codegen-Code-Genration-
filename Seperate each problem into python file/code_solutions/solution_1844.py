import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/title/tt0149096/reviews"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# print(soup.prettify())

# print(soup.find('div', class_='lister-list'))

# print(soup.find('div', class_='lister-list'))