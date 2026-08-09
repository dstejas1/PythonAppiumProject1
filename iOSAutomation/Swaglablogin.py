import time

from appium.options.ios import XCUITestOptions
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from appium.webdriver.appium_service import AppiumService

desired_caps = {
    "platformName": "iOS",
    "platformVersion": "26.5",
    "deviceName": "iPhone 16 Pro",
    "udid": "B57D299A-6602-4DC6-8C41-473AF8B46923",
    "automationName": "XCUITest",
    "app": "/Users/tejasd/Documents/iOS/iOS.Simulator.SauceLabs.Mobile.Sample.app.2.7.1.app"
}
appium_server= AppiumService()
appium_server.start()
options = XCUITestOptions().load_capabilities(desired_caps)

driver = webdriver.Remote(
    "http://127.0.0.1:4723",
    options=options
)

driver.find_element(AppiumBy.ACCESSIBILITY_ID,'test-Username').send_keys('standard_user')
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'test-Password').send_keys('secret_sauce')
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'test-Login').click()

time.sleep(4)
driver.quit()
appium_server.stop()
