from selenium import webdriver
from selenium.webdriver import ActionChains
import time

email = "admin9@gmail.com"
password = "Admin@21"


driver = webdriver.Edge(executable_path="./driver/msedgedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www2.hm.com/en_gb/login")

time.sleep(1)
driver.find_element_by_id('onetrust-accept-btn-handler').click()
time.sleep(1)

# # send keys to input boxes
driver.find_element_by_id('email').send_keys(email)
driver.find_element_by_id('password').send_keys(password)

# Click on login Button
driver.find_element_by_class_name('LoginForm--formSubmit__c-zrD').click()

# Scrap Information
time.sleep(3)
driver.find_element_by_class_name('CTA-module--fullWidth__1GZ-5').click()
time.sleep(3)
cardNumber = driver.find_element_by_class_name('CardBack--codeNumber__3sowW')

with open("cardnumber.txt", 'a') as f:
    f.writelines(f"Login Card Number = {cardNumber.text}")

time.sleep(4)

driver.find_element_by_class_name('ModalTitle--closeButton__1wvri').click()

time.sleep(3)

# Perform Mouse Action
admin = driver.find_elements_by_class_name('menu__myhm')
signOut = driver.find_element_by_xpath('/html/body/header/nav/ul[1]/li[1]/div/div[2]/ul/li[3]/a')

""" Actions To Perform with Mouse """
actions = ActionChains(driver)

""" 1. Mouse Hover"""
# Hover and Click -perform() is necessary to perform click action
actions.move_to_element(admin[1]).move_to_element(signOut).click().perform()

# close browser
driver.close()

