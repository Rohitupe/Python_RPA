from selenium import webdriver


def sign_up(email, password, date_type, first_name, last_name, gender, postal_code):
    driver = webdriver.Edge(executable_path="./driver/msedgedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.google.com")
    driver.find_element_by_name('q').send_keys(first_name+" "+last_name)


def login_user(email, password):
    driver = webdriver.Edge(executable_path="./driver/msedgedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://in.yahoo.com/")
    driver.find_element_by_name('p').send_keys(email + " " + password)
