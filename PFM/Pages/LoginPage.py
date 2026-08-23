import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By


class LoginPageProp:

    def __init__(self, driver):
        self.driver = driver

        self.signUpLoginBtn = 'Sign up'
        self.EmailField = "//*[@value='Enter email address']"
        self.PasswordField = "//*[@value='Enter password']"
        self.ContinueBtn = 'Continue'
        self.usernameField = "//*[@value='Enter username']"
        self.checkbox = 'unSelected'
        self.signUpBtn = 'Sign up'

    def ClickSignUpBtn(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.signUpLoginBtn).click()

    def SignUp(self):
        self.driver.find_element(By.XPATH, self.EmailField).send_keys("qatest17@gmail.com")
        self.driver.find_element(By.XPATH, self.PasswordField).send_keys("Testing@123")
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.ContinueBtn).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.usernameField).send_keys("qatest17")
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.checkbox).click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, self.signUpBtn).click()
