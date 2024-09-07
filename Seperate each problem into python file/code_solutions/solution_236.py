import urllib.request
import urllib.parse
import urllib.error

def get_url(url):
    try:
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        return response.read()
    except urllib.error.URLError as e:
        if hasattr(e, 'code