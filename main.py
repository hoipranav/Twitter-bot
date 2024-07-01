from selenium import webdriver
from bot import HomePage, LoginPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
homepage = HomePage(driver)
loginpage = homepage.load_homepage()
loginpage.login()

driver.close()
