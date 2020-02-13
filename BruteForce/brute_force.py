from selenium import webdriver
import json
import os.path

with open(os.path.join(os.path.dirname(__file__), "data", "staff.txt"), "r+") as tf:
    staff = [t.strip() for t in tf.readlines()]

staff_usernames = {}
for s in staff:
    un = s.split(" ")
    un = (un[-1] + un[0][0]).lower().replace("-", "").replace("'", "")
    if un in staff_usernames:
        staff_usernames[un]+=1
    else:
        staff_usernames[un] = 1

browser = webdriver.Chrome()
def attempt_login(u, p):
    browser.get("https://accounts.veracross.eu/asb/portals/login")
    browser.find_element_by_id("username").send_keys(u)
    browser.find_element_by_id("password").send_keys(p)
    browser.find_element_by_id("recaptcha").click()
    browser.implicitly_wait(2)

for k, v in staff_usernames.items():
    browser.get("https://accounts.veracross.eu/asb/portals/login")
    attempt_login(k, "asbindia")
    if v > 1:
        for i in range(2, v+1):
            attempt_login(k+str(i), "asbindia")

