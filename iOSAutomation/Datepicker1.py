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
    "app": "/Users/tejasd/Library/Developer/Xcode/DerivedData/UIKitCatalog-cykpnfbggdpjqcgegnfvdehfvyys/Build/Products/Debug-iphonesimulator/UIKitCatalog.app"
}

options = XCUITestOptions().load_capabilities(desired_caps)

driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=options
)

driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Date Picker').click()
time.sleep(3)
driver.find_element(By.XPATH,'(//*[@type="XCUIElementTypeButton"])[3]').click()
time.sleep(3)
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'30').click()

time.sleep(5)
driver.quit()
