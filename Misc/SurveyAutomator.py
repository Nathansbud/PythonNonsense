from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

browser = webdriver.Chrome()
browser.get("https://app.collegepulse.com/external-survey/5e71267cc7759d00146bcc69?snowballsample=true&ref=snowball-oa7pdef3f92gf7m9")
browser.implicitly_wait(5)

for i in range(40):
    try:
        browser.find_element_by_class_name("option-box").click()
    except NoSuchElementException:
        pass
    browser.find_element_by_class_name("next-indicator-container").click()
    time.sleep(1)