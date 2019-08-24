from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import atexit
import os
import json


with open(os.path.dirname(__file__) + os.sep + "credentials" + os.sep + "creds.json") as jf:
    creds = json.load(jf)

def make_chrome_browser(path_to, run_headless=False, quit_on_done=False):
    if run_headless:
        headless_options = webdriver.ChromeOptions()
        headless_options.add_argument("headless")
        headless_options.add_argument("incognito")
        b = webdriver.Chrome(executable_path=path_to, options=headless_options)
    else:
        opts = webdriver.ChromeOptions()
        opts.add_argument("incognito")
        b = webdriver.Chrome(executable_path=path_to, options=opts)
    b.implicitly_wait(2)
    WebDriverWait(b, 10)

    if quit_on_done: atexit.register(b.close)

    return b

driver = make_chrome_browser(path_to="/Users/zackamiton/Resources/chromedriver", run_headless=True)
driver.get("https://accounts.epicgames.com/login")

email_box = driver.find_element_by_id("epic_username")
email_box.send_keys(creds['email'])

password_box = driver.find_element_by_id("password")
password_box.send_keys(creds['password'])

submit_btn = driver.find_element_by_id("signIn")
submit_btn.click()

free_game = driver.find_element_by_xpath("//a[starts-with(@class,'FreeGame')]")
driver.get(free_game.get_attribute("href"))

purchase_button = driver.find_element_by_xpath("//button[contains(@class, 'PurchaseButton-button')]")
if not purchase_button.get_attribute("disabled"):
    purchase_button.click()
else:
    print("Game has already been redeemed!")

if __name__ == '__main__':
    pass
