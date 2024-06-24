from selenium import webdriver
from bot import HomePage, LoginPage

driver = webdriver.Chrome()

homepage = HomePage(driver)
loginpage = homepage.load_homepage()
loginpage.login()

driver.close()
