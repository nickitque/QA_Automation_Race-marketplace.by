from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()


browser.get("http://127.0.0.1:8000/login/")
rt22 = browser.find_element(By.CSS_SELECTOR, "#username")
rt22.send_keys("ssss")

browser.find_element(By.CSS_SELECTOR, "#password").send_keys("ddd")
time.sleep(5)