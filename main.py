from selenium import webdriver
from bot import HomePage, LoginPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

homepage = HomePage(driver)
loginpage = homepage.load_homepage()
loginpage.login()

driver.close()
