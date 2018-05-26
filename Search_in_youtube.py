import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://www.youtube.com/')

search = browser.find_element_by_name('query')
search.send_keys("python")
search.send_keys(Keys.RETURN)
time.sleep(5)
browser.quit()