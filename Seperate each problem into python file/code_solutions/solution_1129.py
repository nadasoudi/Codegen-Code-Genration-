import requests

url = "https://en.wikipedia.org/wiki/Python"

response = requests.get(url)

print(response.text)

print(response.status_code)

print(response.headers)

print(response.headers.get('Content-Type'))

print(response.headers.get('Content-Language'))

print(response.headers.get('Content-Language', '