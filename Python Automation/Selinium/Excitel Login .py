from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('/chromedriver.exe')
# driver.get('http://192.168.1.1/admin/login.asp')
driver.get('http://192.168.1.'
           '1')
time.sleep(2)
username_field = driver.find_element('xpath', '''/html/body/main/section[2]/blockquote[1]/form/table/tbody/tr/td/table/tbody/tr[1]/td[3]/font/input''')
username_field.send_keys('excitel')
time.sleep(1)
password_field = driver.find_element('xpath', "/html/body/main/section[2]/blockquote[1]/form/table/tbody/tr/td/table/tbody/tr[2]/td[3]/font/input")
password_field.send_keys("exc@123")
time.sleep(1)
password_field.send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element('xpath', '''/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]/ul/li[2]/div''').click()
time.sleep(1)
driver.find_element('xpath', '/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]/ul/li[2]/ul/li[3]/div').click()
time.sleep(2)
try:
    # driver.find_element('xpath', '''/html/body/section/form/div[1]/table/tbody/tr[1]/td/label''').click()
    driver.find_element(By.ID, 'checkbox0').click()
    time.sleep(1)
    # driver.find_element('xpath','''/html/body/section/form/div[2]''').click()
except:
    # print('Failed on checkbox')
    # driver.find_element('xpath', '/html/body/section/form/div[1]/table/tbody/tr[1]/td/input[1]').click()
    # driver.fsind_element(By.ID, 'checkbox0').click()
    time.sleep(2)
    input("Press enter to close the browser")
    driver.quit()

input("Press enter to close the browser")
driver.quit()


