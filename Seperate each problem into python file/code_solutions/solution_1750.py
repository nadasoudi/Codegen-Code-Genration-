import requests

url = "https://www.python.org/blogs/python-dev/"

# Open the URL in a browser
browser = requests.get(url)

# Print the status code of the response
print(browser.status_code)

# Print the content of the response
print(browser.content)

# Print the headers of the response
print(browser.headers)

# Print the headers of the response
print(browser.headers)

# Print the content of the response
print