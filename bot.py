from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

def sign_in(driver):
    '''Locates Sign in button & clicks it'''
    sign_in_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[4]/a')
    return sign_in_button

def put_username(driver):
    '''Tracks username input, then sends username and clicks next'''
    username = driver.find_element(By.NAME, "text")
    username.clear()
    username.send_keys(os.environ['username'])
    next_button = driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]")
    return next_button

def email_needed(driver):
    '''Checks if email is needed for login, 
    if yes then tracks email input and clicks next'''
    email = driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
    email.clear()
    email.send_keys(os.environ['email'])
    driver.implicitly_wait(1)     
    email_next_button = driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button")
    return email_next_button

def put_password(driver):
    '''Tracks password input, sends password and logs in'''
    password = driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
    password.clear()
    password.send_keys(os.environ['password'])
    driver.implicitly_wait(1)          
    log_in_button = driver.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button")
    return log_in_button
    
def handle_login(driver):
    '''Handles Exceptions during User Account Login'''
    try:
        email_needed(driver).click()
    except:
        put_password(driver).click()
    else:
        put_password(driver).click()
    finally:
        return True

class HomePage:
    '''Use to load the Home Page'''
    def __init__(self, driver):
        self.driver = driver

    def load_homepage(self):
        self.driver.get('https://x.com/')
        self.driver.implicitly_wait(3)
        login_page = LoginPage(self.driver)
        return login_page

class LoginPage:
    '''Use to load the Login Page &  login purposes'''
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        '''Log's in into the User's Twitter Account'''
        x_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/button')
        x_button.click()
        sign_in(self.driver).click()
        self.driver.implicitly_wait(3)
        put_username(self.driver).click()

        if handle_login(self.driver):
            sleep(10)
