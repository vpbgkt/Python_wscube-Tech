from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
s = Service("C:/Users/vpbgk/Downloads/Compressed/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("www.google.com")
time.sleep(6)
print("hi")