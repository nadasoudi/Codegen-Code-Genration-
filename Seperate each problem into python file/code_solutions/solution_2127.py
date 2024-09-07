import urllib.request
import urllib.parse
import urllib.error

url = "http://www.python.org"

# Open the URL in a new tab and specify the user agent
# This will allow us to download the page
request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

# Read the response
response = urllib.request.urlopen(request)

# Print