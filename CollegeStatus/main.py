from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions

import atexit
import json
import os

def make_chrome_browser(run_headless=False, quit_on_done=False):
    options = webdriver.ChromeOptions()
    if run_headless: options.add_argument("headless")
    b = webdriver.Chrome(options=options)
    b.implicitly_wait(2)
    WebDriverWait(b, 10)
    if quit_on_done: atexit.register(b.quit)
    return b

browser = make_chrome_browser(run_headless=True, quit_on_done=True)

with open(os.path.join(os.path.dirname(__file__), "credentials.json")) as cf, open(os.path.join(os.path.dirname(__file__), "schools.json")) as sf:
    creds = json.load(cf)
    schools = json.load(sf)

for s in schools:
    browser.get(schools[s]['url'])
    browser.find_element_by_id("email").send_keys(creds['email'])
    browser.find_element_by_id("password").send_keys(creds[schools[s]['password']])
    browser.find_element_by_class_name('default').click()

    try:
        admissions_checklist = browser.find_element_by_id('part_admissions')
    except selenium.common.exceptions.NoSuchElementException:
        try:
            admissions_checklist = browser.find_element_by_id('part_checklist_Material')
        except selenium.common.exceptions.NoSuchElementException:
            admissions_checklist = None

    print(f"[{s}: {schools[s]['url']}]")
    if admissions_checklist:
        admissions_items = [tr for tr in admissions_checklist.find_elements_by_tag_name("tr") if tr.get_attribute('class') != "column"]
        for item in admissions_items:
            print(item.text)
    else:
        print("Found no application materials!")

