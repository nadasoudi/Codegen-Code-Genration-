import re

def check_title(page):
    if re.search(r'^[A-Za-z0-9_]+$', page):
        return True
    else:
        return False

page = input("Enter the page to check: ")

if check_title(page):
    print("Title contains a word")
else:
    print("Title does not contain a word")

# Solution:

# import re

# def check_title