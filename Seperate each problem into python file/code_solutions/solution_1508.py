import re

def get_language_names(url):
    language_names = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for link in soup.find_all('a', class_='wikitable'):
        language_names.append(link.text)
    return language_names

def get_number_of_related_articles(url):