import time

import allure
import appium
import pytest

from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

def get_data():
    return [
        ("qatest3", "qatest3@trustgrid.com"),
        # ("qatest2", "qatest2@trustgrid.com")
    ]


def setup_function():
    global appium_server
    # appium_server = AppiumService()
    # appium_server.start()
    desired_caps = {
        "platformName": "iOS",
        "platformVersion": "26.5",
        "deviceName": "iPhone 16 Pro",
        "udid": "B57D299A-6602-4DC6-8C41-473AF8B46923",
        "automationName": "XCUITest",
        "app": "/Users/tejasd/Documents/iOS/Verve.app"
       # "app": "/Users/tejasd/Library/Developer/Xcode/DerivedData/UIKitCatalog-cykpnfbggdpjqcgegnfvdehfvyys/Build/Products/Debug-iphonesimulator/UIKitCatalog.app"
    }

    global driver

    options = XCUITestOptions().load_capabilities(desired_caps)

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    time.sleep(3)


@pytest.mark.parametrize("username,email", get_data())
def test_applaunch(username,email):
    print("app is launched")
    time.sleep(3)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Sign up').click()
    driver.find_element(By.XPATH, "//*[@value='Enter email address']").send_keys(email)
    driver.find_element(By.XPATH, "//*[@value='Enter password']").send_keys("Test@123")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Continue').click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@value='Enter username']").send_keys(username)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'unSelected').click()
    time.sleep(1)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Sign up').click()
    allure.attach(driver.get_screenshot_as_png(), name="image2", attachment_type=allure.attachment_type.PNG)

def teardown_function():
    driver.quit()
    # appium_server.stop()





