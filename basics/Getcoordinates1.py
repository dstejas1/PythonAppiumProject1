import time
from concurrent.futures import thread

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

desired_caps = {
    "platformName": "Android",
    "platformVersion": "15",
    "deviceName": "TejasEmulator",
    "automationName": "UiAutomator2",
    "app": "/Users/tejasd/Downloads/android.wdio.native.app.v2.2.0.apk",
    "appActivity": "com.wdiodemoapp.MainActivity"
}

options = UiAutomator2Options().load_capabilities(desired_caps)

driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=options
)
time.sleep(2)
size1= driver.get_window_size()
print(size1)
size2= driver.get_window_rect()
print(size2)

time.sleep(5)
driver.quit()
