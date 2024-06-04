import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
url = "https://www.globalsqa.com/demo-site/datepicker/"
driver.get(url)
driver.maximize_window()
time.sleep(3) # Let the user actually see something!

date_field = driver.find_element("id", "datepicker")
# search_box.send_keys('priti bhushan fuse')
date_field.click()

def click_element():
    pass

time.sleep(5) # Let the user actually see something!

# driver.quit()