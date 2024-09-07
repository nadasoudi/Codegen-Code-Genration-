import requests

url = "http://httpbin.org/get"

response = requests.get(url)

print(response.text)

print(response.json())

print(response.headers)

print(response.cookies)

print(response.status_code)

print(response.encoding)

print(response.content)

print(response.headers.get('