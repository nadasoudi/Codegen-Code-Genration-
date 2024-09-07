import urllib.request
import urllib.parse
import urllib.error

def get_count(url):
    try:
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        count = int(response.read().decode('utf-8'))
        return count
    except urllib.error.HTTPError as e:
        print(e)