from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from csv import DictWriter
import time

def sign_up(email, password, date_type, first_name, last_name, gender, postal_code):
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
    driver.find_element_by_name('day').send_keys(date_type.day)
    driver.find_element_by_name('month').send_keys(date_type.month)
    driver.find_element_by_name('year').send_keys(date_type.year)

    # fill other details
    driver.find_element_by_class_name('CollapseContent-module--toggle__2bUVK').click()

    driver.find_element_by_id('firstName').send_keys(first_name)
    driver.find_element_by_id('lastName').send_keys(last_name)

    # select gender
    dropdown = Select(driver.find_element_by_id('gender'))
    dropdown.select_by_visible_text(gender)

    driver.find_element_by_id('postalCode').send_keys(postal_code)

    time.sleep(1)
    driver.find_element_by_name('hmNewsSubscription').click()

    # Click on login Button
    driver.find_element_by_class_name('RegisterForm--submit__2Enwx').click()

    # Scrap Information
    time.sleep(3)
    driver.find_element_by_class_name('CTA-module--fullWidth__1GZ-5').click()
    time.sleep(3)

    cardNumber = driver.find_element_by_class_name('CardBack--codeNumber__3sowW')
    points = driver.find_element_by_xpath("//div[@class='CardBack--pointsContainer__2fDtk']/span[2]")

    # write to csv and text file
    write_to_text(cardNumber, points, email, "SignUP")
    write_to_excel(cardNumber, points, email)

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

    time.sleep(5)

    # close browser
    driver.close()



def login_user(email, password):
    driver = webdriver.Edge(executable_path="./driver/msedgedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www2.hm.com/en_gb/login")

    time.sleep(1)
    driver.find_element_by_id('onetrust-accept-btn-handler').click()
    time.sleep(1)

    # send keys to input boxes
    driver.find_element_by_id('email').send_keys(email)
    driver.find_element_by_id('password').send_keys(password)

    # Click on login Button
    driver.find_element_by_class_name('LoginForm--formSubmit__c-zrD').click()

    # Scrap Information
    time.sleep(3)
    driver.find_element_by_class_name('CTA-module--fullWidth__1GZ-5').click()
    time.sleep(3)

    cardNumber = driver.find_element_by_class_name('CardBack--codeNumber__3sowW')
    points = driver.find_element_by_xpath("//div[@class='CardBack--pointsContainer__2fDtk']/span[2]")

    # write to text file
    write_to_text(cardNumber, points, email, "Login")

    time.sleep(4)

    driver.find_element_by_class_name('ModalTitle--closeButton__1wvri').click()

    time.sleep(3)

    # Perform Mouse Action
    admin = driver.find_element_by_xpath("//div[@class='account parbase']/a[2]")
    signOut = driver.find_element_by_xpath('/html/body/header/nav/ul[1]/li[1]/div/div[2]/ul/li[3]/a')

    """ Actions To Perform with Mouse """
    actions = ActionChains(driver)

    """ 1. Mouse Hover"""
    # Hover and Click -perform() is necessary to perform click action
    actions.move_to_element(admin).move_to_element(signOut).click().perform()

    # close browser
    driver.close()


def write_to_text(cardNumber, points, email, page):

    with open("H&M.txt", 'a') as f:
        f.writelines(
            f"{page} Loyalty card number = {cardNumber.text},\tPoints balance = {points.text} --> for user with email '{email}'\n"
        )


def write_to_excel(cardNumber, points, email):

    with open("H&M.csv", 'a', newline='') as csvF:
        csv_writer = DictWriter(csvF, fieldnames=["Loyalty card number", "Points balance", "Email Id"])
        if csvF.tell() == 0:
            csv_writer.writeheader()
        csv_writer.writerow({
            "Loyalty card number": cardNumber.text,
            "Points balance": points.text,
            "Email Id": email
        })