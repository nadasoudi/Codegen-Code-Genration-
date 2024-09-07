import urllib.request
import urllib.parse
import urllib.error

def main():
    url = "http://python.org/"
    print("Retrieving", url)
    uh = urllib.request.urlopen(url)
    data = uh.read()
    print("Retrieved", len(data), "characters")
    print("Total", len(data), "characters")
    print("Count:",