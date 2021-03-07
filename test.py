from selenium import webdriver
from selenium.webdriver.support.ui import Select
from datetime import date
import time

email = "rohit@gmmail.com"
password = "Rohit21@data"
first_name = "Rohit"
last_name = "Tupe"
gender = "Male"
postal_code = "123455"
date = date.today()



driver = webdriver.Edge(executable_path="./driver/msedgedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www2.hm.com/en_gb/register")

time.sleep(1)
driver.find_element_by_id('onetrust-accept-btn-handler').click()
time.sleep(1)

# send keys to input boxes
driver.find_element_by_id('email').send_keys(email)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_name('day').send_keys(date.day)
driver.find_element_by_name('month').send_keys(date.month)
driver.find_element_by_name('year').send_keys(date.year)

# fill other details
driver.find_element_by_class_name('CollapseContent-module--toggle__2bUVK').click()

driver.find_element_by_id('firstName').send_keys(first_name)
driver.find_element_by_id('lastName').send_keys(last_name)

# select gender
dropdown = Select(driver.find_element_by_id('gender'))
# dropdown.select_by_value()
dropdown.select_by_visible_text(gender)

driver.find_element_by_id('postalCode').send_keys('W1F7NU')

time.sleep(1)
driver.find_element_by_name('hmNewsSubscription').click()