import requests
from bs4 import BeautifulSoup

url = "https://www.indeed.com/jobs?q=python&l=San%20Francisco,%20CA&radius=100&start=0"

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

# print(soup.prettify())

# print(soup.title)

# print(soup.title.string)

# print(soup