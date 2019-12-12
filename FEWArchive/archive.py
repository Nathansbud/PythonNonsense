import tweepy
from os import sep
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import atexit
import json
import os

with open("credentials" + sep + "twitter.json") as jf: creds = json.load(jf)

login_page = "https://twitter.com/login"
account_timeline = "https://twitter.com/fckeveryword"

def make_chrome_browser(run_headless=False, quit_on_done=False):
    options = webdriver.ChromeOptions()
    if run_headless: options.add_argument("headless")
    b = webdriver.Chrome(options=options)
    b.implicitly_wait(2)
    WebDriverWait(b, 10)
    if quit_on_done: atexit.register(b.close)
    return b

browser = make_chrome_browser(quit_on_done=False)
browser.get(login_page)
email_field = browser.find_element_by_class_name("js-username-field")
email_field.send_keys(creds['email'])

password_field = browser.find_element_by_class_name("js-password-field")
password_field.send_keys(creds['password'])

login_button = browser.find_element_by_class_name("EdgeButtom--medium")
login_button.click()

browser.get(account_timeline)
for tweet in browser.find_elements_by_tag_name("article"):
    print(tweet)

