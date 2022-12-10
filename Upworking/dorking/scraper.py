from selenium import webdriver
from selenium.webdriver.support import expected_conditions
import time


google_url = "https://google.com/search?q="
with open('emails.txt') as ef: emails = [email.strip() for email in ef.readlines()]



def make_browser(headless=False):
    options = webdriver.ChromeOptions()
    if headless: options.add_argument("headless")

    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(3)
    return browser

def dork_emails():
    browser = make_browser()
    for email in emails[30:]:
        browser.get(f'{google_url}"{email}"')
        no_results = browser.find_elements_by_xpath("//div[@aria-level='2']") or browser.find_elements_by_xpath("//p[text()='No results containing all your search terms were found.']")
        if no_results:
            print(f"No content found for {email}")
            continue
        else:
            print(f"Listings for {email}:")
            listings = browser.find_elements_by_class_name("g")
            for l in listings:
                header = l.find_element_by_class_name('r').find_element_by_tag_name('a')
                title, url = header.text, header.get_attribute('href')
                body = l.find_element_by_class_name('s').text
                print(title, url, body)

if __name__ == '__main__':
    dork_emails()
    pass