python solution.py

"""

import requests
import bs4

def get_html(url):
    r = requests.get(url)
    return r.text

def get_soup(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    return soup

def get_h1_tags(soup):
    h1_tags = soup.find_all