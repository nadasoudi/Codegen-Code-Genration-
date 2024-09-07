import requests
from bs4 import BeautifulSoup

url = "https://www.reddit.com/r/Python/comments/2qjvx/python_solution_to_scrape_the_reddit_comments_in_python/"

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

comments = soup.find_all('div', class_='comments-list-item')

for comment in comments:
    print(comment