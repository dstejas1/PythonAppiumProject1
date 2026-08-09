import time
import requests
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

desired_caps = {
    "platformName": "Android",
    "platformVersion": "15",
    "deviceName": "TejasEmulator",
    "automationName": "UiAutomator2",
    "app": "/Users/tejasd/Downloads/callsandroid.apk"
}


options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

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
driver.find_element(
    AppiumBy.XPATH,
    "//*[@text='Allow']"
).click()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@text='']").click()




time.sleep(20)
