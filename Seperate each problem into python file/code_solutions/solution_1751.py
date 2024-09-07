import urllib.request
import urllib.parse
import urllib.error

def main():
    # Open the URL
    url = input('Enter - ')
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)

    # Read the data from the URL and print it out.
    data = uh.read()
    print('Retrieved', len(data), 'characters')

    # Close the connection
    uh.close()