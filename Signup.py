from selenium import webdriver

driver = webdriver.Edge(executable_path="")
driver.implicitly_wait(10)
driver.maximize_window()


# def run():
driver.get("")