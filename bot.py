from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os
from dotenv import load_dotenv

load_dotenv()

class HomePage:
    "Use to load the Home Page"
    def __init__(self, driver):
        self.driver = driver

    def load_homepage(self):
        self.driver.get('https://x.com/')
        self.driver.implicitly_wait(3)
        login_page = LoginPage(self.driver)
        return login_page

class LoginPage:
    "Use to load the Login Page &  login purposes"
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        sign_in_button = self.driver.find_element(By.LINK_TEXT, 'Sign in')
        sign_in_button.click()
        self.driver.implicitly_wait(5)
        username = self.driver.find_element(By.NAME, "text")
        username.clear()
        username.send_keys(os.environ['username'])
        next_button = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]")
        next_button.click()
        email = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]")
        email.clear()
        email.send_keys(os.environ['email'])
        email_next_button = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button")
        email_next_button.click()
        password = self.driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div")
        password.clear()
        password.send_keys(os.environ['password'])
