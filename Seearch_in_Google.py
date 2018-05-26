import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('http://www.google.com')

search = browser.find_element_by_name('q')
search.send_keys('youtube')
search.send_keys(Keys.RETURN)
time.sleep(5)
browser.quit()
