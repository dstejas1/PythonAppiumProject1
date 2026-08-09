import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

desired_caps = {
    "platformName": "iOS",
    "platformVersion": "18.7.9",
    "deviceName": "iPhone 16 Pro",
    "udid": "00008020-001A4C282E91002E",
    "automationName": "XCUITest",
    "app": "/Users/tejasd/Downloads/TrustGridSocial.ipa"
}

options = XCUITestOptions().load_capabilities(desired_caps)

driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=options
)
time.sleep(10)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Accept').click()
time.sleep(2)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, ' Dive back in!').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@text="Enter handle"]').send_keys("robin")
time.sleep(2)
pin1 = driver.find_element(AppiumBy.XPATH, '(//android.widget.EditText)[2]')
pin2 = driver.find_element(AppiumBy.XPATH, '(//android.widget.EditText)[3]')
pin3 = driver.find_element(AppiumBy.XPATH, '(//android.widget.EditText)[4]')
pin4 = driver.find_element(AppiumBy.XPATH, '(//android.widget.EditText)[5]')
pin5 = driver.find_element(AppiumBy.XPATH, '(//android.widget.EditText)[6]')
pin6 = driver.find_element(AppiumBy.XPATH, '(//android.widget.EditText)[7]')

pin1.send_keys("1")
pin2.send_keys("4")
pin3.send_keys("7")
pin4.send_keys("2")
pin5.send_keys("5")
pin6.send_keys("8")

driver.find_element(By.XPATH,"//*[@content-desc='Dive back in']").click()
time.sleep(6)


time.sleep(5)
driver.quit()