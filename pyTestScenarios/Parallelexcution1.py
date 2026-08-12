import time

import appium
import pytest

from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService

@pytest.fixture(params=["device1","device2"], scope="function")
def before_each_function(request):
    global driver
    if request.param=="device1":
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
            "http://127.0.0.1:4724",
            options=options
        )
        time.sleep(3)


    if request.param=="device2":
        desired_caps = {
            "platformName": "iOS",
            "platformVersion": "26.5",
            "deviceName": "iPhone 17 Pro",
            "udid": "CB0CB78C-1A34-431D-9AF6-333AAA2E3630",
            "automationName": "XCUITest",
            "app":    "/Users/tejasd/Documents/iOS/Verve.app"
        }


        options = XCUITestOptions().load_capabilities(desired_caps)

        driver = webdriver.Remote(
            "http://127.0.0.1:4723",
            options=options
        )
        time.sleep(3)

    yield
    print("end driver connection")
    driver.quit()

@pytest.mark.usefixtures("before_each_function")
def test_logout():
        print("test_logout")
