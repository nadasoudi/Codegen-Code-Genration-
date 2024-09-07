import requests
from bs4 import BeautifulSoup

url = "https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

top_stories = soup.find_all('a', class_='CfkVc')

for story in top_stories:
    print(story.get('href'