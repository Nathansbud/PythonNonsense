import os
import json
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException
import time

with open(os.path.join(os.path.dirname(__file__), "credentials", "instagram.json")) as jf: creds = json.load(jf)
browser = webdriver.Chrome()
browser.implicitly_wait(10)

browser.get("https://www.instagram.com/")
inputs = browser.find_elements_by_tag_name("input")
inputs[0].send_keys(creds['username'])
inputs[1].send_keys(creds['password'])
browser.find_element_by_xpath("//button[@type='submit']").click()
notif_dialog = browser.find_element_by_xpath("//div[@role='dialog']")
notif_dialog.find_elements_by_tag_name("button")[1].click()

elements = browser.find_elements_by_tag_name("a")
for f in elements:
    if f.text.strip() == "Watch All":
        f.click()
        break
else:
    print("Failed to find story watch button; quitting...")
    browser.quit()

b = browser.find_element_by_xpath("//button[div/@class='coreSpriteRightChevron']")

while "stories" in browser.current_url:
    story_elements = browser.find_elements_by_xpath("//div[@role='button']")[2:]
    try:
        if len(story_elements) > 0:
            se = list(filter(None, [s.text for s in story_elements]))
            if len(se) > 0:
                print(se)
                if "\n" in se[-1] and se[-1].endswith("%"): print("Finished poll")
                else: print("Unfinished poll")
        right_arrow = browser.find_element_by_xpath("//button[div/@class='coreSpriteRightChevron']")
        right_arrow.click()
    except StaleElementReferenceException:
        print("Some (page-changing related) shit hit the fan (is you still a fan?)")
    except ElementClickInterceptedException:
        print("Some (unclickable element) shit hit the fan (is you still a fan?)")


