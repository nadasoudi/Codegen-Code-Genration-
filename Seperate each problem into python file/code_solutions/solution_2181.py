import urllib.request
import os

url = "https://www.python.org/ftp/python/3.8.5/python-3.8.5-amd64.exe"

print("Downloading: " + url)

try:
    response = urllib.request.urlopen(url)
    print("File Downloaded")
except urllib.error.URLError as e:
    print("Error:", e.reason)

print("Done")