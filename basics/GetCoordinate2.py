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
#signUp
driver.find_element(By.XPATH,'//android.widget.Button[@content-desc="Login"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//android.widget.TextView[@text="Sign up"]').click()
time.sleep(2)
obj= driver.find_element(By.XPATH,'//*[@text="SIGN UP"]')
loc= obj.location
x_cor= loc['x']
y_cor= loc['y']

dim= obj.size
w= dim['width']
h= dim['height']
center_x= x_cor+(w/2)
center_y= y_cor+(h/2)
print(center_x,center_y)
time.sleep(5)
driver.quit()
