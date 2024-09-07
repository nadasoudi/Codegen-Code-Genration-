import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Open the browser
browser = webdriver.Chrome()

# Open the website
browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# Find the input box
input_box = browser.find_element_by_id('sldNumber')

# Send the input value to the input box
input_box.send