import json

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


def make_browser(headless=False):
    options = webdriver.ChromeOptions()
    if headless: options.add_argument("headless")

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    return browser

def login(browser, credentials):
    browser.get('https://integratedcomputersolutions.atlassian.net/login')
    browser.find_element_by_id('username').send_keys(credentials.get('username') or '')
    browser.find_element_by_id('login-submit').click()
    browser.find_element_by_id('password').send_keys(credentials.get('password') or '')
    browser.find_element_by_id('login-submit').click()

if __name__ == '__main__':
    with open("tickets.txt") as tf, open('credentials/jira.json') as cf:
        tickets = [int(l) for l in tf.readlines()]
        credentials = json.load(cf)
    
    browser = make_browser()
    login(browser, credentials)
    
    cu = browser.current_url
    WebDriverWait(browser, 15).until(EC.url_changes(cu))

    for i, t in enumerate(tickets):
        ticket_url = f"https://integratedcomputersolutions.atlassian.net/browse/SSV-{t}"
        browser.get(ticket_url)
        try:
            WebDriverWait(browser, 10).until(EC.url_changes(ticket_url))
            print(ticket_url, browser.current_url)
        except TimeoutException:
            print(ticket_url, "(Does Not Exist)")

