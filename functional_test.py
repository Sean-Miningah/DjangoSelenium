from selenium import webdriver

browser = webdriver.Firefox()  # Starting a Selenium "webdriver" to start a Firefox browser
browser.get('http://localhost:8000')

assert 'Django' in browser.title  # Checking that we have the word Django in the page title
