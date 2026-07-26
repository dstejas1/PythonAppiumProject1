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

driver.find_element(By.XPATH,'//android.widget.TextView[@text="Web"]').click()
time.sleep(4)
contexts= driver.contexts

for context in contexts:
    print(context)
driver.switch_to.context("WEBVIEW_com.wdiodemoapp")
driver.find_element(By.XPATH,'//button[@class="DocSearch DocSearch-Button"]').click()

time.sleep(5)
driver.quit()
