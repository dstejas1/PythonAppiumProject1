import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

desired_caps = {
    "platformName": "iOS",
    "platformVersion": "26.5",
    "deviceName": "iPhone 16 Pro",
    "udid": "B57D299A-6602-4DC6-8C41-473AF8B46923",
    "automationName": "XCUITest",
    "app": "/Users/tejasd/Downloads/TestApp.app",
}

options = XCUITestOptions().load_capabilities(desired_caps)

driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=options
)

time.sleep(5)
driver.quit()