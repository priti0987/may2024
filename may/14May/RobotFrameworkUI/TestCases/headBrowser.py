import base64
import os
from selenium import webdriver


def open_my_browser(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()

