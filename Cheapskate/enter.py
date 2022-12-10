from selenium import webdriver
import time

x = webdriver.Safari()
x.implicitly_wait(4)

if __name__ == "__main__":
    for i in range(10000):
        x.get("https://www.cartoonnetwork.com/promos/202011_gibson/")
        x.find_element_by_id('email').send_keys(f'zamiton+{i}@outlook.com')
        x.find_element_by_id('submit').click()
        time.sleep(0.5)