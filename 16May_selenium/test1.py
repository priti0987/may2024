import os
import time
from datetime import date

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = "https://demo.automationtesting.in/Datepicker.html"
driver.get(url)
# time.sleep(5)
driver.maximize_window()
time.sleep(2)
# driver.switch_to.frame(driver.find_elements(By.XPATH,"//iframe[@class='demo-frame lazyloaded']"))
# time.sleep(2)
print("pass til here")

driver.find_element(By.XPATH, "//input[@id='datepicker1']").click()

time.sleep(2)
print("done..!")
today_day = ((date.today().day))
today_day = str(today_day)
# time.sleep(5)
#
driver.find_element(By.XPATH, "//a[contains(text(),'"+today_day+"')]").click()
time.sleep(3)
# driver.find_element(By.XPATH, "//body/nav[@id='m-codechef-nav']/div[1]/div[2]/div[2]/a[1]/span[1]").click()
# time.sleep(10)
#
# driver.switch_to.frame("webklipper-publisher-widget-container-notification-frame")
# driver.find_element(By.XPATH, "(//button[@id='3d81c465'])[1]").click()
# time.sleep(5)
#
# driver.switch_to.default_content()
# time.sleep(5)
#
# current = driver.window_handles
# driver.switch_to.window(driver.current_window_handle)
# time.sleep(10)
#
# driver.find_element(By.XPATH, "//a[contains(text(),'Sleep deprivation')]").click()
# time.sleep(5)
#
# driver.get("https://www.codechef.com/submit/SLEEP")
#
# cur = driver.window_handles
# driver.switch_to.window(driver.current_window_handle)
# time.sleep(30)
#
# element = WebDriverWait(driver, 10)
# element.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Submit Code')]"))
#
# # element = WebDriverWait(driver, 10).until(
# #      EC.presence_of_element_located((By.XPATH,"//button[contains(text(),'Submit Code')]"))
# #   )
# # element.click()