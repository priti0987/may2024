import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()

driver.get("http://www.naukri.com")
driver.maximize_window()
login = driver.find_element("id", "login_Layer")
# search_box.send_keys('priti bhushan fuse')
login.click()
time.sleep(5) # Let the user actually see something!

# driver.quit()