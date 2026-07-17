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

driver.find_element(By.XPATH,'//android.widget.Button[@content-desc="Forms"]').click()
time.sleep(2)
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'switch').click()
time.sleep(3)
driver.find_element(By.XPATH,'//android.view.ViewGroup[@content-desc="Dropdown"]').click()
time.sleep(3)
dropdown_options= driver.find_elements(By.ID,'android:id/text1')
len(dropdown_options)
for value in dropdown_options:
    ele_text = value.get_attribute('text')
    print(ele_text)

    if ele_text =="This app is awesome":
        print("desired option is displayed")
        value.click()
        break


time.sleep(5)
driver.quit()
