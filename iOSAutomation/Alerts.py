import time
from sys import implementation

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
    "app": "/Users/tejasd/Library/Developer/Xcode/DerivedData/UIKitCatalog-cykpnfbggdpjqcgegnfvdehfvyys/Build/Products/Debug-iphonesimulator/UIKitCatalog.app"
}

options = XCUITestOptions().load_capabilities(desired_caps)

driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=options
)
driver.implicitly_wait(40)
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Alert Views').click()
time.sleep(1)
#simple Alert

#Okay / Cancel
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Okay / Cancel').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Cancel').click()

#Other
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Other').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Cancel').click()

#Text Entry
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Text Entry').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Cancel').click()

#Secure Text Entry
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Secure Text Entry').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Cancel').click()

#Confirm / Cancel
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Confirm / Cancel').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Confirm').click()

#Destructive
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Destructive').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Safe Choice').click()

time.sleep(5)
driver.quit()
