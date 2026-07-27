import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

desired_caps = {
    "platformName": "iOS",
    "platformVersion": "26.5",
    "deviceName": "iPhone 16 Pro",
    "udid": "B57D299A-6602-4DC6-8C41-473AF8B46923",
    "automationName": "XCUITest",
    "app": "/Users/tejasd/Documents/iOS/Verve.app"
}

options = XCUITestOptions().load_capabilities(desired_caps)

driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=options
)
time.sleep(3)
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Sign up').click()
driver.find_element(By.XPATH,"//*[@value='Enter email address']").send_keys("dstejas2@gmail.com")
driver.find_element(By.XPATH,"//*[@value='Enter password']").send_keys("Test@123")
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Continue').click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[@value='Enter username']").send_keys("dstejas1")
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'unSelected').click()
time.sleep(1)
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Sign up').click()


time.sleep(5)
driver.quit()